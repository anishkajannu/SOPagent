"""Index the controlled documents in ./sops into a persistent local vector store.

Reads every .md, .docx and .pdf under ./sops (recursively), extracts the text,
and indexes it. So you can just DROP a new or updated SOP into ./sops and run
`python ingest.py` again — no manual conversion needed.

Document metadata (number / title / type) comes from the file NAME. Two naming
schemes are understood:
  * Official QMS numbering:  "SOP-006 Deviation Management.docx",
    "WIN-001 Pre-Download Readiness.pdf", "QM-001 Quality Manual.md"
  * Older NM scheme:  "NM-OPS-DAT-002-v1.0 Customer Data Backup Procedure.md"

Rules:
  * Forms and templates (FRM-*, TMP-*) are skipped — they're blank, not content.
  * If the same document number appears more than once (e.g. a .pdf in an archive
    folder AND an edited .md), the MOST RECENTLY MODIFIED file wins, so your
    latest version is the one indexed. Only the winner is read.
"""

import re
from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

OFFICIAL_PATTERN = re.compile(
    r"^(?P<doc_number>(?:QM|SOP|POL|WIN|MAN|FRM|TMP)-\d{3}(?:-\d{2})?)\s+(?P<title>.+)\.\w+$"
)
NM_PATTERN = re.compile(
    r"^(?P<doc_number>[A-Z]+-[A-Z]+-[A-Z]+-\d+-v[\d.]+)\s+(?P<title>.+)\.\w+$"
)

READABLE_EXTENSIONS = {".md", ".docx", ".pdf"}
SKIP_TYPES = {"FRM", "TMP"}                 # forms and templates: blank, not content
EXT_PREFERENCE = {".md": 0, ".pdf": 1, ".docx": 2}  # tiebreak when mtimes are equal

# Header/footer boilerplate to strip from extracted Word/PDF text.
_BOILER = [
    r"^Zoho Sign Document ID", r"^STANDARD OPERATING PROCEDURE$", r"^WORK INSTRUCTION$",
    r"^QUALITY MANUAL$", r"^MANUAL$", r"^POLICY$", r"^Document Number:", r"^Effective Date:",
    r"^Version Number:", r"^Page:\s", r"^Title:", r"^Page \d+ of \d+$", r"^\d+ of \d+$",
    r"THIS DOCUMENT CONTAINS CONFIDENTIAL",
]
_BOILER_RE = [re.compile(p) for p in _BOILER]


def parse_name(name: str) -> tuple[str, str, str]:
    """Return (doc_number, title, doc_type) from a file name."""
    nm = NM_PATTERN.match(name)
    if nm:
        return nm["doc_number"], nm["title"], "NM"
    official = OFFICIAL_PATTERN.match(name)
    if official:
        return official["doc_number"], official["title"], official["doc_number"].split("-")[0]
    return "UNKNOWN", Path(name).stem, "UNKNOWN"


def _strip_boiler(text: str) -> str:
    kept = [ln.rstrip() for ln in text.split("\n")
            if ln.strip() and not any(rx.search(ln.strip()) for rx in _BOILER_RE)]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(kept)).strip()


def extract_text(path: Path) -> str:
    """Extract plain text from a .md, .docx or .pdf file."""
    ext = path.suffix.lower()
    if ext == ".md":
        return path.read_text(encoding="utf-8")
    if ext == ".docx":
        import docx  # from python-docx
        d = docx.Document(str(path))
        parts = [p.text for p in d.paragraphs]
        for table in d.tables:
            for row in table.rows:
                parts.append("\t".join(cell.text for cell in row.cells))
        return _strip_boiler("\n".join(parts))
    if ext == ".pdf":
        import pdfplumber
        pages = []
        with pdfplumber.open(str(path)) as pdf:
            for page in pdf.pages:
                pages.append(page.extract_text() or "")
        return _strip_boiler("\n".join(pages))
    return ""


def load_doc(path: Path) -> Document:
    doc_number, title, doc_type = parse_name(path.name)
    meta = {"doc_number": doc_number, "title": title, "doc_type": doc_type,
            "source_file": path.name}
    return Document(page_content=extract_text(path), metadata=meta)


def choose_files(sops_dir: Path) -> list[Path]:
    """Pick one file per document number: newest wins, then prefer .md > .pdf > .docx."""
    best: dict[str, tuple] = {}
    for path in sops_dir.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in READABLE_EXTENSIONS:
            continue
        doc_number, _, doc_type = parse_name(path.name)
        if doc_type in SKIP_TYPES:
            continue
        # higher score wins: newest mtime, then preferred extension, then shallower path
        score = (path.stat().st_mtime, -EXT_PREFERENCE[path.suffix.lower()], -len(path.parts))
        if doc_number not in best or score > best[doc_number][0]:
            best[doc_number] = (score, path)
    return [entry[1] for entry in best.values()]


def build_stable_ids(chunks: list[Document]) -> list[str]:
    """Every chunk gets an ID so re-indexing updates existing entries instead of duplicating."""
    seen_counts: dict[str, int] = {}
    ids = []
    for chunk in chunks:
        doc_number = chunk.metadata.get("doc_number", "UNKNOWN")
        i = seen_counts.get(doc_number, 0)
        ids.append(f"{doc_number}::chunk-{i}")
        seen_counts[doc_number] = i + 1
    return ids


def main() -> None:
    files = sorted(choose_files(Path("./sops")), key=lambda p: p.name)
    docs = [load_doc(p) for p in files]
    docs = [d for d in docs if d.page_content.strip()]  # drop anything that yielded no text

    splitter = RecursiveCharacterTextSplitter(
        separators=["\n## ", "\n### ", "\n\n", "\n", " "],
        chunk_size=800,
        chunk_overlap=120,
    )
    chunks = splitter.split_documents(docs)
    ids = build_stable_ids(chunks)

    embeddings = FastEmbedEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    sop_store = Chroma(
        collection_name="netramind_sops",
        embedding_function=embeddings,
        persist_directory="./chroma_sops",
    )
    sop_store.add_documents(chunks, ids=ids)
    print(f"Indexed {len(chunks)} chunks from {len(docs)} documents into ./chroma_sops")
    for d in docs:
        print(f"  {d.metadata['doc_number']:16} {d.metadata['source_file']}")


if __name__ == "__main__":
    main()

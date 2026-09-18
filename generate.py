"""Generate a new controlled SOP as a Word (.docx) document.

Pipeline (structure & numbers = code, prose = LLM):
  1. Assign the next OFFICIAL document number for the series (e.g. SOP-033).
  2. Retrieve related SOP context from the existing Chroma store (grounding).
  3. Ask the model for the prose of each section as structured output.
  4. Render the Netramind house-style .docx and write ./sops/<number> <title>.docx.

The result is a DRAFT for author/QA review, never an approved document.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import TypedDict

from langchain.chat_models import init_chat_model
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from sop_docx import build_sop_docx, _clean_title

SOPS_DIR = Path("./sops")
MODEL = "anthropic:claude-sonnet-5"  # same model string as main.py

# Official controlled-document numbering (Attachment A): SOP-031, WIN-003, QM-001, ...
DOC_NUMBER_RE = re.compile(r"\b(?P<type>QM|SOP|POL|WIN|MAN)-(?P<num>\d{3})\b")


class Responsibility(TypedDict):
    """One role and the specific duties it owns (renders as 5.1 role, 5.1.1 duty…)."""

    role: str
    duties: list[str]


class ProcedureStep(TypedDict):
    """One procedure step and its detailed sub-actions (renders as 6.1 step, 6.1.1 substep…)."""

    step: str
    substeps: list[str]


class SOPDraft(TypedDict):
    """Structured prose the model returns. Section numbering is NOT the model's job."""

    title: str
    purpose: str
    scope: str
    definitions: list[str]
    responsibilities: list[Responsibility]
    procedure: list[ProcedureStep]
    references: list[str]


def next_doc_number(doc_type: str = "SOP", sops_dir: Path = SOPS_DIR) -> str:
    """Return the next official document number in a series, e.g. 'SOP-033'.

    Scans every file AND folder name under ./sops so existing documents and
    archive folders both count, then adds one to the highest number for this type.
    """
    doc_type = doc_type.upper()
    highest = 0
    for path in sops_dir.rglob("*"):
        for m in DOC_NUMBER_RE.finditer(path.name):
            if m.group("type") == doc_type:
                highest = max(highest, int(m.group("num")))
    return f"{doc_type}-{highest + 1:03d}"


def related_context(topic: str, k: int = 4) -> str:
    """Pull related passages from the existing SOP store so tone and cross-references match."""
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    store = Chroma(
        collection_name="netramind_sops",
        embedding_function=embeddings,
        persist_directory="./chroma_sops",
    )
    hits = store.similarity_search(topic, k=k)
    if not hits:
        return "(No related SOPs found in the store.)"
    blocks = []
    for doc in hits:
        num = doc.metadata.get("doc_number", "UNKNOWN")
        title = doc.metadata.get("title", "Unknown title")
        blocks.append(f"[{num} — {title}]\n{doc.page_content}")
    return "\n\n---\n\n".join(blocks)


def draft_sections(topic: str, doc_number: str, context: str) -> SOPDraft:
    """Ask the model to write the prose for each section, grounded in existing SOPs."""
    model = init_chat_model(MODEL).with_structured_output(SOPDraft)
    prompt = (
        "You are drafting a new Netramind Standard Operating Procedure (SOP). Follow "
        "the Netramind controlled-document format EXACTLY, matching the style and "
        "structure of the existing SOPs shown below.\n"
        f"Document number (already assigned, do not change): {doc_number}\n"
        f"Topic requested: {topic}\n\n"
        "Formatting and content rules (follow all):\n"
        "- 'title': the subject only (e.g. 'Deviation Management'). Do NOT include the "
        "document number in the title.\n"
        "- Write in present tense, one actor per action, concise and specific to Netramind.\n"
        "- 'definitions': a list of 'Term — meaning' entries. Define EVERY acronym or "
        "term used anywhere in the SOP, in alphabetical order.\n"
        "- 'responsibilities': one entry per role. Each entry has a 'role' (the role name, "
        "e.g. 'Quality Assurance (QA) or Designee') and a 'duties' list of that role's "
        "specific duties. These render as 5.1 role, 5.1.1 duty, 5.1.2 duty, and so on.\n"
        "- 'procedure': an ordered list of steps. Each entry has a 'step' (the high-level "
        "step) and a 'substeps' list breaking it into detailed sub-actions. Use substeps "
        "whenever a step involves more than one action or decision — prefer a nested "
        "structure (6.1 step, 6.1.1 substep, 6.1.2 substep) over long single steps. If a "
        "step is genuinely atomic, give it an empty 'substeps' list.\n"
        "- 'references': related Netramind documents (by number and title) and any external "
        "standards. Do NOT invent regulatory citations; only cite standards you are given.\n"
        "- Ground everything in the related SOPs below; reuse their terminology and cross-"
        "reference them by document number where relevant.\n\n"
        "Related SOPs for grounding:\n"
        f"{context}"
    )
    return model.invoke(prompt)


def generate_sop(
    topic: str,
    doc_type: str = "SOP",
    sops_dir: Path = SOPS_DIR,
) -> dict:
    """Generate a new controlled-document draft as .docx and write it to ./sops.

    Returns {"doc_number", "title", "path"}. `doc_type` is the series to number
    within (SOP, WIN, POL, MAN, QM). The written file is a DRAFT.
    """
    sops_dir.mkdir(exist_ok=True)
    doc_number = next_doc_number(doc_type, sops_dir)
    context = related_context(topic)
    draft = draft_sections(topic, doc_number, context)

    title = _clean_title(draft["title"].strip())
    path = sops_dir / f"{doc_number} {title}.docx"
    # base_dir is the project root (parent of ./sops) so the logo is found
    build_sop_docx(doc_number, draft, str(path), base_dir=str(sops_dir.parent))
    return {"doc_number": doc_number, "title": title, "path": str(path)}


if __name__ == "__main__":
    topic = input("What should the new SOP cover? ")
    doc_type = (input("Document type [SOP]: ").strip() or "SOP").upper()
    result = generate_sop(topic, doc_type)
    print(f"\nDrafted {result['doc_number']} -> {result['path']}")
    print("This is a DRAFT (Word document) for author/QA review. It still needs approval before use.")

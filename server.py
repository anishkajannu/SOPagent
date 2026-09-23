"""FastAPI backend for the Netramind SOP Assistant.

Why FastAPI instead of Streamlit: visiting the page serves plain static files and
does NOT import the agent, so the UI paints instantly even while the container is
cold. The heavy AI stack (embedding model, Chroma, LangChain agent) is imported
lazily on the first /chat request via get_agent().

Endpoints
  GET  /health                 -> liveness check (no agent import)
  GET  /api/ready              -> whether the agent is warmed up yet
  POST /api/chat/stream        -> streams the answer token-by-token (NDJSON)
  GET  /api/sops               -> list of documents in ./sops
  GET  /api/sops/preview       -> formatted preview (HTML for .docx, else markdown)
  GET  /api/sops/download      -> download a document
  GET  /                       -> static/index.html (+ /static assets)

Run locally:   uvicorn server:app --reload --port 8000
"""

from __future__ import annotations

import base64
import html as html_lib
import json
import re
import shutil
import time
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, Query, UploadFile
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import mammoth

# NOTE: heavy imports (ingest -> langchain/chroma, and main -> the agent) are done
# lazily inside the functions that need them, so importing this module — and thus
# starting uvicorn and serving the static UI — stays fast.

SOPS_DIR = Path("./sops")
STATIC_DIR = Path("./static")
LOGO_PATH = Path("netramind_logo.png")
DRAFT_MARKER = "pending QA approval"
VIEWABLE_SUFFIXES = {".md", ".docx", ".pdf"}

_FNAME_RE = re.compile(r"^((?:SOP|WIN|MAN|QM|POL|FRM|TMP|NM)-\d{3})\s+(.*)$", re.I)
_DOCNUM_RE = re.compile(r"\b((?:SOP|WIN|MAN|QM|POL|FRM|TMP|NM)-\d{3}[\w-]*)")
_HEADING_RE = re.compile(r"^\d+\s+[A-Z][A-Z /&]+$")
_HEADING_WORDS = {"REFERENCES", "DEFINITIONS", "RESPONSIBILITIES", "PROCEDURE",
                  "PURPOSE", "SCOPE", "ATTACHMENTS", "REVISION HISTORY", "SIGNATURE PAGE"}

app = FastAPI(title="Netramind SOP Assistant")

# In-process conversation memory, keyed by a session id the browser generates.
# Lost on restart (same as the old Streamlit session) — fine for this use.
_SESSIONS: dict[str, list] = {}

# The agent (and everything heavy it pulls in) is imported only on first use.
_AGENT = None
_AIMessageChunk = None


def get_agent():
    """Import and build the agent lazily so page loads stay instant."""
    global _AGENT, _AIMessageChunk
    if _AGENT is None:
        from main import agent
        from langchain_core.messages import AIMessageChunk
        _AGENT = agent
        _AIMessageChunk = AIMessageChunk
    return _AGENT


# ----------------------------------------------------------------- helpers
def _extract_cached(path: Path) -> str:
    from ingest import extract_text  # deferred: pulls in langchain/chroma
    return extract_text(path)


def _is_draft(path: Path) -> bool:
    try:
        return DRAFT_MARKER.lower() in _extract_cached(path).lower()
    except Exception:
        return False


def _safe_doc(name: str) -> Path:
    """Resolve a document name to a real file inside ./sops (blocks path traversal)."""
    p = (SOPS_DIR / name).resolve()
    if p.parent != SOPS_DIR.resolve() or not p.is_file():
        raise HTTPException(status_code=404, detail="Document not found")
    return p


def _logo_data_uri() -> str:
    if not LOGO_PATH.exists():
        return ""
    return "data:image/png;base64," + base64.b64encode(LOGO_PATH.read_bytes()).decode()


def _doc_header(path: Path) -> str:
    m = _FNAME_RE.match(path.stem)
    doc_number, title = (m.group(1).upper(), m.group(2)) if m else ("", path.stem)
    logo = _logo_data_uri()
    logo_html = f"<img class='logo' src='{logo}'/>" if logo else "<div class='logo'></div>"
    return (
        "<div class='dochead'>"
        f"{logo_html}"
        "<table class='meta'>"
        "<tr><td colspan='2' class='sop'>STANDARD OPERATING PROCEDURE</td></tr>"
        f"<tr><td class='lbl'>Document Number:</td><td>{html_lib.escape(doc_number)}</td></tr>"
        f"<tr><td class='lbl'>Title:</td><td>{html_lib.escape(title)}</td></tr>"
        "</table></div>"
    )


def _docx_preview_html(path: Path) -> str:
    """Full-fidelity HTML for a .docx: headings, underlines, tables, red refs, header banner."""
    with open(path, "rb") as f:
        body = mammoth.convert_to_html(f, style_map="u => u").value
    body = body.replace("\t", "<span class='tab'></span>")

    def redden(m: re.Match) -> str:
        inner = _DOCNUM_RE.sub(r"<span class='ref'>\1</span>", m.group(1))
        return f"<p class='bullet'>•{inner}</p>"
    body = re.sub(r"<p>•(.*?)</p>", redden, body, flags=re.S)

    return f"""<!doctype html><html><head><meta charset='utf-8'><style>
      body {{ margin:0; background:#eef0f4; }}
      .page {{ background:#fff; max-width:820px; margin:16px auto; padding:40px 54px;
               box-shadow:0 1px 6px rgba(0,0,0,.15);
               font-family:Calibri,'Segoe UI',Arial,sans-serif; font-size:15px;
               color:#1a1a1a; line-height:1.45; }}
      .dochead {{ display:flex; align-items:center; gap:22px; padding-bottom:14px;
                  border-bottom:2px solid #1a56db; margin-bottom:22px; }}
      .dochead .logo {{ height:46px; }}
      table.meta {{ border-collapse:collapse; margin-left:auto; font-size:12.5px; }}
      table.meta td {{ border:1px solid #333; padding:3px 9px; }}
      table.meta .sop {{ text-align:center; font-weight:600; letter-spacing:.3px; }}
      table.meta .lbl {{ text-align:right; font-weight:600; white-space:nowrap; }}
      .page p {{ margin:5px 0; }}
      .page strong {{ font-size:15.5px; }}
      .page table {{ border-collapse:collapse; width:100%; margin:10px 0 16px; font-size:13.5px; }}
      .page table td, .page table th {{ border:1px solid #444; padding:5px 8px; text-align:left; }}
      .page .bullet {{ margin:3px 0; }}
      .ref {{ color:#c00000; }}
      .tab {{ display:inline-block; width:1.6em; }}
    </style></head><body>
      <div class='page'>{_doc_header(path)}{body}</div>
    </body></html>"""


def _markdown_preview(path: Path) -> str:
    """Tidy markdown for .md and .pdf (client renders it)."""
    if path.suffix.lower() == ".md":
        return path.read_text(encoding="utf-8", errors="ignore")
    from ingest import extract_text  # deferred
    out = []
    for raw in extract_text(path).split("\n"):
        s = raw.replace("\t", " ").strip()
        if not s:
            continue
        out.append(f"### {s}" if (_HEADING_RE.match(s) or s in _HEADING_WORDS) else s)
    return "\n\n".join(out)


def _chunk_text(msg) -> str:
    content = getattr(msg, "content", "")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for b in content:
            if isinstance(b, dict) and b.get("type") == "text":
                parts.append(b.get("text", ""))
            elif isinstance(b, str):
                parts.append(b)
        return "".join(parts)
    return ""


def _docx_names() -> set[str]:
    return {p.name for p in SOPS_DIR.glob("*.docx")}


# ------------------------------------------------------------------- API
@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/ready")
def ready():
    """Whether the agent is already warmed up (so the UI can label the first call)."""
    return {"ready": _AGENT is not None}


class ChatRequest(BaseModel):
    message: str
    session_id: str


@app.post("/api/chat/stream")
def chat_stream(req: ChatRequest):
    """Stream the assistant's answer as NDJSON: {"delta": "..."} lines, then a
    final {"done": true, "new_docx": <name|null>} line."""

    def gen():
        try:
            agent = get_agent()
        except Exception as e:  # import/build failure (e.g. missing API key)
            yield json.dumps({"error": f"Could not start the assistant: {e}"}) + "\n"
            return

        history = _SESSIONS.get(req.session_id, [])
        history = list(history)
        history.append({"role": "user", "content": req.message})

        before = _docx_names()
        answer = ""
        final_state = None
        try:
            for mode, chunk in agent.stream(
                {"messages": history}, stream_mode=["messages", "values"]
            ):
                if mode == "messages":
                    msg, _meta = chunk
                    if isinstance(msg, _AIMessageChunk):
                        piece = _chunk_text(msg)
                        if piece:
                            answer += piece
                            yield json.dumps({"delta": piece}) + "\n"
                elif mode == "values":
                    final_state = chunk
        except Exception as e:
            yield json.dumps({"error": f"The assistant hit an error: {e}"}) + "\n"
            return

        if final_state and final_state.get("messages"):
            _SESSIONS[req.session_id] = final_state["messages"]
        else:
            history.append({"role": "assistant", "content": answer})
            _SESSIONS[req.session_id] = history

        new = sorted(_docx_names() - before)
        yield json.dumps({"done": True, "new_docx": (new[-1] if new else None)}) + "\n"

    return StreamingResponse(gen(), media_type="application/x-ndjson")


# Matches both numbering schemes, incl. a -NN suffix (e.g. MAN-018-02) and the NM scheme.
_DOCNUM_PREFIX = re.compile(
    r"^((?:QM|SOP|POL|WIN|MAN|FRM|TMP)-\d{3}(?:-\d{2})?|[A-Z]+-[A-Z]+-[A-Z]+-\d+-v[\d.]+)", re.I)


def _doc_number_of(filename: str) -> str | None:
    m = _DOCNUM_PREFIX.match(Path(filename).stem)
    return m.group(1).upper() if m else None


def _doc_sort_key(p: Path):
    dn = _doc_number_of(p.name)
    return (0, dn) if dn else (1, p.name.lower())  # numbered docs first, in order; rest after


@app.get("/api/sops")
def list_sops():
    files = [p for p in SOPS_DIR.glob("*") if p.suffix.lower() in VIEWABLE_SUFFIXES]
    files.sort(key=_doc_sort_key)  # document-number order (SOP-001, SOP-002, …)
    items = []
    for p in files:
        m = _FNAME_RE.match(p.stem)
        items.append({
            "name": p.name,
            "doc_number": (m.group(1).upper() if m else ""),
            "title": (m.group(2) if m else p.stem),
            "suffix": p.suffix.lower().lstrip("."),
            "is_draft": _is_draft(p),
            "mtime": p.stat().st_mtime,
        })
    return {"documents": items}


@app.get("/api/sops/preview")
def preview_sop(name: str = Query(...)):
    path = _safe_doc(name)
    if path.suffix.lower() == ".docx":
        return JSONResponse({"type": "html", "html": _docx_preview_html(path)})
    return JSONResponse({"type": "markdown", "text": _markdown_preview(path)})


@app.get("/api/sops/download")
def download_sop(name: str = Query(...)):
    path = _safe_doc(name)
    return FileResponse(str(path), filename=path.name)


# ---- Manage: upload new/updated SOPs, archive obsolete ones, rebuild the index ----
UPLOAD_SUFFIXES = {".docx", ".pdf", ".md"}


def _archive_move(path: Path) -> Path:
    """Move a file into ./sops/_archive without clobbering an existing archived copy."""
    archive = SOPS_DIR / "_archive"
    archive.mkdir(exist_ok=True)
    dest = archive / path.name
    if dest.exists():
        dest = archive / f"{path.stem}__{int(time.time())}{path.suffix}"
    shutil.move(str(path), str(dest))
    return dest


@app.post("/api/sops/upload")
async def upload_sops(files: list[UploadFile] = File(...)):
    """Save uploaded SOPs into ./sops. Uploading a new version of a document
    auto-archives any existing file with the SAME document number, so the old
    version is retired automatically (kept in _archive, excluded from the index)."""
    SOPS_DIR.mkdir(exist_ok=True)
    saved, skipped, auto_archived = [], [], []
    for f in files:
        name = Path(f.filename or "").name  # strip any path components
        if not name or Path(name).suffix.lower() not in UPLOAD_SUFFIXES:
            skipped.append(name or "(unnamed)")
            continue
        # Auto-archive prior versions of the same document (any different filename).
        dn = _doc_number_of(name)
        if dn:
            for existing in list(SOPS_DIR.glob("*")):
                if (existing.is_file() and existing.name != name
                        and existing.suffix.lower() in UPLOAD_SUFFIXES
                        and _doc_number_of(existing.name) == dn):
                    _archive_move(existing)
                    auto_archived.append(existing.name)
        with open(SOPS_DIR / name, "wb") as out:
            out.write(await f.read())
        saved.append(name)
    return {"saved": saved, "skipped": skipped, "auto_archived": auto_archived}


class NameReq(BaseModel):
    name: str


@app.post("/api/sops/archive")
def archive_sop(req: NameReq):
    """Move a document into ./sops/_archive — kept on disk for records, excluded from the index."""
    path = _safe_doc(req.name)
    _archive_move(path)
    return {"archived": path.name}


@app.post("/api/rebuild")
def rebuild_index():
    """Clean rebuild: wipe the index and re-index only the current ./sops files.
    Also resets open chat sessions so answers reflect the new index immediately.
    Returns the manifest (what is now indexed + timestamp) for audit evidence."""
    import ingest  # deferred: pulls in langchain/chroma + the embedding model
    try:
        manifest = ingest.rebuild(SOPS_DIR)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Rebuild failed: {e}")
    _SESSIONS.clear()  # drop conversation memory so stale answers aren't re-served
    return manifest


@app.get("/api/manifest")
def get_manifest():
    """The most recent rebuild manifest (what the assistant is currently running on)."""
    p = Path("./index_manifest.json")
    if p.exists():
        try:
            return JSONResponse(json.loads(p.read_text()))
        except Exception:
            pass
    return JSONResponse({"documents": [], "rebuilt_at": None, "document_count": 0})


@app.get("/")
def index():
    """Serve the app shell. This does NOT import the agent, so it returns instantly."""
    return FileResponse(str(STATIC_DIR / "index.html"))


# /static/* -> the static directory (style.css, app.js, marked.min.js, …).
if STATIC_DIR.is_dir():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

"""Simple web UI for the Netramind SOP assistant.

Run it with:   streamlit run app.py
It opens in your browser at http://localhost:8501

Left tab  = chat with the assistant (search SOPs, draft new ones, ask about regs).
Right tab = browse and read every SOP with its real Word formatting, and any
            freshly generated draft is pinned on top.
"""

import base64
import html
import re
from pathlib import Path

import mammoth
import streamlit as st
import streamlit.components.v1 as components

# Importing main builds the agent, embeddings and vector store once.
from main import agent
from ingest import extract_text
from gov import ALLOWED_DOMAINS  # official domains -> style those citations

SOPS_DIR = Path("./sops")
DRAFT_MARKER = "pending QA approval"
VIEWABLE = ("*.md", "*.docx", "*.pdf")
LOGO_PATH = Path("netramind_logo.png")

# A document-number token (SOP-034, WIN-003 …) -> rendered in red like the real refs.
_DOCNUM_RE = re.compile(r"\b((?:SOP|WIN|MAN|QM|POL|FRM|TMP|NM)-\d{3}[\w-]*)")
# Pull "SOP-034" and the title out of a filename like "SOP-034 Following Direction.docx".
_FNAME_RE = re.compile(r"^((?:SOP|WIN|MAN|QM|POL|FRM|TMP|NM)-\d{3})\s+(.*)$", re.I)

# Lines that should render as section headings in the .md / .pdf fallback preview.
_HEADING_RE = re.compile(r"^\d+\s+[A-Z][A-Z /&]+$")
_HEADING_WORDS = {"REFERENCES", "DEFINITIONS", "RESPONSIBILITIES", "PROCEDURE",
                  "PURPOSE", "SCOPE", "ATTACHMENTS", "REVISION HISTORY", "SIGNATURE PAGE"}

# ---- Citation styling: green pills for Netramind SOPs, blue for official sources ----
_MD_LINK = re.compile(r"\[([^\]]+)\]\((https?://[^\s)]+)\)")
_RAW_URL = re.compile(r"https?://[^\s<>()]+")
_CITE_DOCNUM = re.compile(r"\b((?:SOP|WIN|MAN|QM|POL|FRM|TMP|NM)-\d{3}(?:-\d{2})?)\b")

_SOP_PILL = ("background:#e6f4ea;color:#137333;border:1px solid #b7e1c4;border-radius:10px;"
             "padding:1px 7px;font-weight:600;font-size:.82em;white-space:nowrap;")
_GOV_PILL = ("background:#e8f0fe;color:#1a56db;border:1px solid #c3d6fb;border-radius:10px;"
             "padding:1px 7px;font-weight:600;font-size:.82em;text-decoration:none;white-space:nowrap;")


def _host(url: str) -> str:
    return re.sub(r"^https?://(www\.)?", "", url).split("/")[0].lower()


def _is_gov(url: str) -> bool:
    h = _host(url)
    return any(h == d or h.endswith("." + d) for d in ALLOWED_DOMAINS)


def style_citations(text: str) -> str:
    """Turn SOP numbers into green pills and official-source links into blue pills."""
    stash: list[str] = []

    def keep(frag: str) -> str:
        stash.append(frag)
        return f"\x00{len(stash) - 1}\x00"   # park finished HTML so later passes skip it

    def md(m: re.Match) -> str:
        label, url = m.group(1), m.group(2)
        if _is_gov(url):
            return keep(f'<a href="{url}" target="_blank" style="{_GOV_PILL}">🏛️ {html.escape(label)}</a>')
        return m.group(0)  # leave non-official links to normal markdown
    text = _MD_LINK.sub(md, text)

    def raw(m: re.Match) -> str:
        url, trail = m.group(0), ""
        while url and url[-1] in ".,;:]}'\")":   # don't swallow trailing punctuation
            trail = url[-1] + trail
            url = url[:-1]
        if _is_gov(url):
            return keep(f'<a href="{url}" target="_blank" style="{_GOV_PILL}">🏛️ {_host(url)}</a>') + trail
        return m.group(0)
    text = _RAW_URL.sub(raw, text)

    text = _CITE_DOCNUM.sub(lambda m: keep(f'<span style="{_SOP_PILL}">📘 {m.group(1)}</span>'), text)

    for i, frag in enumerate(stash):
        text = text.replace(f"\x00{i}\x00", frag)
    return text

st.set_page_config(page_title="Netramind SOP Assistant", page_icon="📘", layout="wide")

st.markdown(
    """
    <style>
      .block-container {padding-top: 2rem;}
      .draft-pill {background:#fdecea; color:#b3261e; padding:2px 8px;
                   border-radius:12px; font-size:0.75rem; font-weight:600;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("📘 Netramind SOP Assistant")
st.caption("Ask about your SOPs, draft new ones, or look up official regulations — all grounded in your controlled documents.")

chat_tab, library_tab = st.tabs(["💬  Assistant", "📄  SOP Library"])


def _mime(path: Path) -> str:
    return {
        ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ".pdf": "application/pdf",
    }.get(path.suffix.lower(), "text/markdown")


@st.cache_data(show_spinner=False)
def _logo_data_uri() -> str:
    """The NetraMind logo as a data: URI so the preview header shows it inline."""
    if not LOGO_PATH.exists():
        return ""
    b64 = base64.b64encode(LOGO_PATH.read_bytes()).decode()
    return f"data:image/png;base64,{b64}"


@st.cache_data(show_spinner=False)
def doc_text(path_str: str, mtime: float) -> str:
    """Plain text of a document (used for the draft check and search)."""
    return extract_text(Path(path_str))


@st.cache_data(show_spinner=False)
def doc_markdown(path_str: str, mtime: float) -> str:
    """A readable Markdown rendering for .md and .pdf (the .docx path uses HTML)."""
    path = Path(path_str)
    if path.suffix.lower() == ".md":
        return path.read_text(encoding="utf-8", errors="ignore")
    out = []
    for raw in extract_text(path).split("\n"):
        s = raw.replace("\t", " ").strip()
        if not s:
            continue
        if _HEADING_RE.match(s) or s in _HEADING_WORDS:
            out.append(f"### {s}")
        else:
            out.append(s)
    return "\n\n".join(out)


def _doc_header(path: Path) -> str:
    """A reconstructed controlled-document header banner (Word headers aren't in the body)."""
    m = _FNAME_RE.match(path.stem)
    doc_number, title = (m.group(1).upper(), m.group(2)) if m else ("", path.stem)
    logo = _logo_data_uri()
    logo_html = f"<img class='logo' src='{logo}'/>" if logo else "<div class='logo'></div>"
    return (
        "<div class='dochead'>"
        f"{logo_html}"
        "<table class='meta'>"
        "<tr><td colspan='2' class='sop'>STANDARD OPERATING PROCEDURE</td></tr>"
        f"<tr><td class='lbl'>Document Number:</td><td>{doc_number}</td></tr>"
        f"<tr><td class='lbl'>Title:</td><td>{title}</td></tr>"
        "</table></div>"
    )


@st.cache_data(show_spinner=False)
def doc_html(path_str: str, mtime: float) -> str:
    """Full-fidelity HTML for a .docx: real headings, underlines, tables, red refs."""
    path = Path(path_str)
    with open(path, "rb") as f:
        body = mammoth.convert_to_html(f, style_map="u => u").value

    # Tabs collapse in HTML; render them as a fixed gap so "4.1  Term" stays aligned.
    body = body.replace("\t", "<span class='tab'></span>")

    # Re-apply the red colour to internal document references inside bullet lines
    # (mammoth drops run colour), matching the printed SOP.
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


def _newest_docx_set():
    return {str(p) for p in SOPS_DIR.glob("*.docx")}


# ---------------------------------------------------------------- Chat tab
with chat_tab:
    if "lc_messages" not in st.session_state:
        st.session_state.lc_messages = []
    if "shown" not in st.session_state:
        st.session_state.shown = []
    if "new_docx" not in st.session_state:
        st.session_state.new_docx = None

    for role, text in st.session_state.shown:
        with st.chat_message(role):
            if role == "assistant":
                st.markdown(style_citations(text), unsafe_allow_html=True)
            else:
                st.markdown(text)

    prompt = st.chat_input("Ask a question, or say “draft an SOP about …”")
    if prompt:
        st.session_state.shown.append(("user", prompt))
        with st.chat_message("user"):
            st.markdown(prompt)

        before = _newest_docx_set()  # snapshot so we can spot a freshly drafted SOP
        st.session_state.lc_messages.append({"role": "user", "content": prompt})
        with st.chat_message("assistant"):
            with st.spinner("Working…"):
                response = agent.invoke({"messages": st.session_state.lc_messages})
                st.session_state.lc_messages = response["messages"]
                last = st.session_state.lc_messages[-1]
                answer = getattr(last, "text", None) or getattr(last, "content", "")
            st.markdown(style_citations(answer), unsafe_allow_html=True)
        st.session_state.shown.append(("assistant", answer))

        new = sorted(_newest_docx_set() - before)
        if new:
            st.session_state.new_docx = new[-1]  # remember the drafted file for the panel below

    # Offer the freshly generated Word file for one-click download, and point to
    # the Library tab where it renders with full formatting.
    new_docx = st.session_state.get("new_docx")
    if new_docx and Path(new_docx).exists():
        p = Path(new_docx)
        st.divider()
        st.success(f"Draft ready:  **{p.stem}**")
        c1, c2 = st.columns([1, 2])
        with c1:
            st.download_button("⬇️  Download Word (.docx)", p.read_bytes(),
                               file_name=p.name, mime=_mime(p),
                               type="primary", use_container_width=True)
        with c2:
            st.caption("It's also pinned at the top of the **📄 SOP Library** tab, "
                       "shown with its full Word formatting.")


# ------------------------------------------------------------- Library tab
with library_tab:
    files = []
    for pattern in VIEWABLE:
        files += SOPS_DIR.glob(pattern)
    files = sorted(files, key=lambda p: p.stat().st_mtime, reverse=True)

    if not files:
        st.info("No documents in ./sops yet. Draft one from the Assistant tab, or add files and run `python ingest.py`.")
    else:
        def is_draft(p: Path) -> bool:
            return DRAFT_MARKER.lower() in doc_text(str(p), p.stat().st_mtime).lower()

        drafts = [p for p in files if is_draft(p)]
        if drafts:
            st.subheader("🆕 Recently generated drafts")
            st.caption("Created by the assistant — still need author / QA review.")

        left, right = st.columns([1, 2], gap="large")
        with left:
            only_drafts = st.checkbox("Show drafts only", value=False)
            shown_files = drafts if only_drafts else files
            choice = st.radio(
                f"Documents ({len(shown_files)})",
                options=range(len(shown_files)),
                format_func=lambda i: ("🆕 " if shown_files[i] in drafts else "")
                + f"{shown_files[i].stem}  ·  {shown_files[i].suffix[1:]}",
            )
            selected = shown_files[choice] if shown_files else None

        with right:
            if selected:
                if selected in drafts:
                    st.markdown("<span class='draft-pill'>DRAFT — pending QA</span>",
                                unsafe_allow_html=True)
                if selected.suffix.lower() == ".docx":
                    # Real Word formatting: headings, underlined terms, tables, red refs.
                    components.html(
                        doc_html(str(selected), selected.stat().st_mtime),
                        height=780, scrolling=True,
                    )
                else:
                    st.markdown(f"### {selected.stem}")
                    with st.container(border=True):
                        st.markdown(doc_markdown(str(selected), selected.stat().st_mtime))
                st.download_button("⬇️  Download this file", selected.read_bytes(),
                                   file_name=selected.name, mime=_mime(selected))

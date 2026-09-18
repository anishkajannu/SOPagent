"""Simple web UI for the Netramind SOP assistant.

Run it with:   streamlit run app.py
It opens in your browser at http://localhost:8501

Left tab  = chat with the assistant (search SOPs, draft new ones, ask about regs).
Right tab = browse and read every SOP, with freshly generated drafts pinned on top.
"""

import re
from pathlib import Path

import streamlit as st

# Importing main builds the agent, embeddings and vector store once.
from main import agent
from ingest import extract_text

SOPS_DIR = Path("./sops")
DRAFT_MARKER = "pending QA approval"
VIEWABLE = ("*.md", "*.docx", "*.pdf")

# Lines that should render as section headings in the preview.
_HEADING_RE = re.compile(r"^\d+\s+[A-Z][A-Z /&]+$")
_HEADING_WORDS = {"REFERENCES", "DEFINITIONS", "RESPONSIBILITIES", "PROCEDURE",
                  "PURPOSE", "SCOPE", "ATTACHMENTS", "REVISION HISTORY", "SIGNATURE PAGE"}

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
def doc_text(path_str: str, mtime: float) -> str:
    """Plain text of a document (used for the draft check and search)."""
    return extract_text(Path(path_str))


@st.cache_data(show_spinner=False)
def doc_markdown(path_str: str, mtime: float) -> str:
    """A readable Markdown rendering, consistent for .md, .docx and .pdf."""
    path = Path(path_str)
    if path.suffix.lower() == ".md":
        return path.read_text(encoding="utf-8", errors="ignore")
    # .docx / .pdf: turn the extracted text into tidy Markdown so it renders
    # like the Markdown SOPs — section titles become headings, tabs become spaces.
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


# ---------------------------------------------------------------- Chat tab
with chat_tab:
    if "lc_messages" not in st.session_state:
        st.session_state.lc_messages = []
    if "shown" not in st.session_state:
        st.session_state.shown = []

    for role, text in st.session_state.shown:
        with st.chat_message(role):
            st.markdown(text)

    prompt = st.chat_input("Ask a question, or say “draft an SOP about …”")
    if prompt:
        st.session_state.shown.append(("user", prompt))
        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.lc_messages.append({"role": "user", "content": prompt})
        with st.chat_message("assistant"):
            with st.spinner("Working…"):
                response = agent.invoke({"messages": st.session_state.lc_messages})
                st.session_state.lc_messages = response["messages"]
                last = st.session_state.lc_messages[-1]
                answer = getattr(last, "text", None) or getattr(last, "content", "")
            st.markdown(answer)
        st.session_state.shown.append(("assistant", answer))


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
                st.markdown(f"### {selected.stem}")
                if selected in drafts:
                    st.markdown("<span class='draft-pill'>DRAFT — pending QA</span>",
                                unsafe_allow_html=True)
                with st.container(border=True):
                    st.markdown(doc_markdown(str(selected), selected.stat().st_mtime))
                st.download_button("Download this file", selected.read_bytes(),
                                   file_name=selected.name, mime=_mime(selected))

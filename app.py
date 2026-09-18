"""Web UI for the Netramind SOP assistant.

Run locally with:
    streamlit run app.py

Performance notes:
- The LangChain agent is loaded lazily only when the user sends a message.
- The SOP library is loaded only when the user explicitly opens it.
- Expensive document parsing is cached.
"""

import base64
import html
import re
from pathlib import Path

import mammoth
import streamlit as st
import streamlit.components.v1 as components

from gov import ALLOWED_DOMAINS
from ingest import extract_text
from langchain_core.messages import AIMessageChunk


# ---------------------------------------------------------------------
# Streamlit page setup
# ---------------------------------------------------------------------

st.set_page_config(
    page_title="Netramind SOP Assistant",
    page_icon="📘",
    layout="wide",
)

SOPS_DIR = Path("./sops")
DRAFT_MARKER = "pending QA approval"
VIEWABLE = ("*.md", "*.docx", "*.pdf")
LOGO_PATH = Path("netramind_logo.png")


# ---------------------------------------------------------------------
# IMPORTANT PERFORMANCE FIX
#
# Do NOT:
#     from main import agent
#
# at the top of this file.
#
# main.py imports LangChain, generation tools, government search, etc.
# We wait until the user actually asks a question.
# ---------------------------------------------------------------------

@st.cache_resource(show_spinner=False)
def get_agent():
    from main import agent
    return agent


# ---------------------------------------------------------------------
# Regex / styling
# ---------------------------------------------------------------------

_DOCNUM_RE = re.compile(
    r"\b((?:SOP|WIN|MAN|QM|POL|FRM|TMP|NM)-\d{3}[\w-]*)"
)

_FNAME_RE = re.compile(
    r"^((?:SOP|WIN|MAN|QM|POL|FRM|TMP|NM)-\d{3})\s+(.*)$",
    re.I,
)

_HEADING_RE = re.compile(r"^\d+\s+[A-Z][A-Z /&]+$")

_HEADING_WORDS = {
    "REFERENCES",
    "DEFINITIONS",
    "RESPONSIBILITIES",
    "PROCEDURE",
    "PURPOSE",
    "SCOPE",
    "ATTACHMENTS",
    "REVISION HISTORY",
    "SIGNATURE PAGE",
}

_MD_LINK = re.compile(r"\[([^\]]+)\]\((https?://[^\s)]+)\)")
_RAW_URL = re.compile(r"https?://[^\s<>()]+")
_CITE_DOCNUM = re.compile(
    r"\b((?:SOP|WIN|MAN|QM|POL|FRM|TMP|NM)-\d{3}(?:-\d{2})?)\b"
)

_SOP_PILL = (
    "background:#e6f4ea;"
    "color:#137333;"
    "border:1px solid #b7e1c4;"
    "border-radius:10px;"
    "padding:1px 7px;"
    "font-weight:600;"
    "font-size:.82em;"
    "white-space:nowrap;"
)

_GOV_PILL = (
    "background:#e8f0fe;"
    "color:#1a56db;"
    "border:1px solid #c3d6fb;"
    "border-radius:10px;"
    "padding:1px 7px;"
    "font-weight:600;"
    "font-size:.82em;"
    "text-decoration:none;"
    "white-space:nowrap;"
)


def _host(url: str) -> str:
    return re.sub(r"^https?://(www\.)?", "", url).split("/")[0].lower()


def _is_gov(url: str) -> bool:
    host = _host(url)
    return any(
        host == domain or host.endswith("." + domain)
        for domain in ALLOWED_DOMAINS
    )


def style_citations(text: str) -> str:
    """Render SOP citations as green pills and official sources as blue pills."""

    stash: list[str] = []

    def keep(fragment: str) -> str:
        stash.append(fragment)
        return f"\x00{len(stash) - 1}\x00"

    def md(match: re.Match) -> str:
        label, url = match.group(1), match.group(2)

        if _is_gov(url):
            return keep(
                f'<a href="{url}" target="_blank" '
                f'style="{_GOV_PILL}">'
                f'🏛️ {html.escape(label)}</a>'
            )

        return match.group(0)

    text = _MD_LINK.sub(md, text)

    def raw(match: re.Match) -> str:
        url = match.group(0)
        trail = ""

        while url and url[-1] in ".,;:]}'\")":
            trail = url[-1] + trail
            url = url[:-1]

        if _is_gov(url):
            return (
                keep(
                    f'<a href="{url}" target="_blank" '
                    f'style="{_GOV_PILL}">'
                    f'🏛️ {_host(url)}</a>'
                )
                + trail
            )

        return match.group(0)

    text = _RAW_URL.sub(raw, text)

    text = _CITE_DOCNUM.sub(
        lambda m: keep(
            f'<span style="{_SOP_PILL}">'
            f'📘 {m.group(1)}</span>'
        ),
        text,
    )

    for i, fragment in enumerate(stash):
        text = text.replace(f"\x00{i}\x00", fragment)

    return text


def _chunk_text(msg) -> str:
    """Get only visible assistant text from a streamed LangChain message."""

    content = getattr(msg, "content", "")

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        parts = []

        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                parts.append(block.get("text", ""))

            elif isinstance(block, str):
                parts.append(block)

        return "".join(parts)

    return ""


# ---------------------------------------------------------------------
# UI styling
# ---------------------------------------------------------------------

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 2rem;
        }

        .draft-pill {
            background: #fdecea;
            color: #b3261e;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 0.75rem;
            font-weight: 600;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("📘 Netramind SOP Assistant")

st.caption(
    "Ask about your SOPs, draft new ones, or look up official regulations "
    "— all grounded in your controlled documents."
)


# ---------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------

def _mime(path: Path) -> str:
    return {
        ".docx": (
            "application/vnd.openxmlformats-officedocument."
            "wordprocessingml.document"
        ),
        ".pdf": "application/pdf",
    }.get(path.suffix.lower(), "text/markdown")


@st.cache_data(show_spinner=False)
def _logo_data_uri() -> str:
    if not LOGO_PATH.exists():
        return ""

    b64 = base64.b64encode(LOGO_PATH.read_bytes()).decode()

    return f"data:image/png;base64,{b64}"


@st.cache_data(show_spinner=False, max_entries=64)
def doc_text(path_str: str, mtime: float) -> str:
    """Plain document text.

    Only called when actually needed.
    """

    return extract_text(Path(path_str))


@st.cache_data(show_spinner=False, max_entries=64)
def doc_markdown(path_str: str, mtime: float) -> str:
    path = Path(path_str)

    if path.suffix.lower() == ".md":
        return path.read_text(
            encoding="utf-8",
            errors="ignore",
        )

    output = []

    for raw in extract_text(path).split("\n"):
        line = raw.replace("\t", " ").strip()

        if not line:
            continue

        if _HEADING_RE.match(line) or line in _HEADING_WORDS:
            output.append(f"### {line}")

        else:
            output.append(line)

    return "\n\n".join(output)


def _doc_header(path: Path) -> str:
    match = _FNAME_RE.match(path.stem)

    if match:
        doc_number = match.group(1).upper()
        title = match.group(2)

    else:
        doc_number = ""
        title = path.stem

    logo = _logo_data_uri()

    if logo:
        logo_html = f"<img class='logo' src='{logo}'/>"
    else:
        logo_html = "<div class='logo'></div>"

    return (
        "<div class='dochead'>"
        f"{logo_html}"
        "<table class='meta'>"
        "<tr>"
        "<td colspan='2' class='sop'>"
        "STANDARD OPERATING PROCEDURE"
        "</td>"
        "</tr>"
        f"<tr><td class='lbl'>Document Number:</td>"
        f"<td>{doc_number}</td></tr>"
        f"<tr><td class='lbl'>Title:</td>"
        f"<td>{title}</td></tr>"
        "</table>"
        "</div>"
    )


@st.cache_data(show_spinner=False, max_entries=64)
def doc_html(path_str: str, mtime: float) -> str:
    """Convert a DOCX to cached HTML."""

    path = Path(path_str)

    with open(path, "rb") as file:
        body = mammoth.convert_to_html(
            file,
            style_map="u => u",
        ).value

    body = body.replace(
        "\t",
        "<span class='tab'></span>",
    )

    def redden(match: re.Match) -> str:
        inner = _DOCNUM_RE.sub(
            r"<span class='ref'>\1</span>",
            match.group(1),
        )

        return f"<p class='bullet'>•{inner}</p>"

    body = re.sub(
        r"<p>•(.*?)</p>",
        redden,
        body,
        flags=re.S,
    )

    return f"""
    <!doctype html>
    <html>
    <head>
        <meta charset='utf-8'>

        <style>
            body {{
                margin: 0;
                background: #eef0f4;
            }}

            .page {{
                background: #fff;
                max-width: 820px;
                margin: 16px auto;
                padding: 40px 54px;
                box-shadow: 0 1px 6px rgba(0,0,0,.15);
                font-family: Calibri, 'Segoe UI', Arial, sans-serif;
                font-size: 15px;
                color: #1a1a1a;
                line-height: 1.45;
            }}

            .dochead {{
                display: flex;
                align-items: center;
                gap: 22px;
                padding-bottom: 14px;
                border-bottom: 2px solid #1a56db;
                margin-bottom: 22px;
            }}

            .dochead .logo {{
                height: 46px;
            }}

            table.meta {{
                border-collapse: collapse;
                margin-left: auto;
                font-size: 12.5px;
            }}

            table.meta td {{
                border: 1px solid #333;
                padding: 3px 9px;
            }}

            table.meta .sop {{
                text-align: center;
                font-weight: 600;
                letter-spacing: .3px;
            }}

            table.meta .lbl {{
                text-align: right;
                font-weight: 600;
                white-space: nowrap;
            }}

            .page p {{
                margin: 5px 0;
            }}

            .page strong {{
                font-size: 15.5px;
            }}

            .page table {{
                border-collapse: collapse;
                width: 100%;
                margin: 10px 0 16px;
                font-size: 13.5px;
            }}

            .page table td,
            .page table th {{
                border: 1px solid #444;
                padding: 5px 8px;
                text-align: left;
            }}

            .page .bullet {{
                margin: 3px 0;
            }}

            .ref {{
                color: #c00000;
            }}

            .tab {{
                display: inline-block;
                width: 1.6em;
            }}
        </style>
    </head>

    <body>
        <div class='page'>
            {_doc_header(path)}
            {body}
        </div>
    </body>
    </html>
    """


def _newest_docx_set():
    return {
        str(path)
        for path in SOPS_DIR.glob("*.docx")
    }


# ---------------------------------------------------------------------
# Navigation
#
# This is intentionally NOT st.tabs().
#
# Streamlit executes the code inside every tab even when the user isn't
# looking at that tab. That meant your library was opening documents
# during startup.
#
# With this selector, only the selected page executes.
# ---------------------------------------------------------------------

page = st.radio(
    "View",
    ["💬 Assistant", "📄 SOP Library"],
    horizontal=True,
    label_visibility="collapsed",
)


# =====================================================================
# CHAT
# =====================================================================

if page == "💬 Assistant":

    if "lc_messages" not in st.session_state:
        st.session_state.lc_messages = []

    if "shown" not in st.session_state:
        st.session_state.shown = []

    if "new_docx" not in st.session_state:
        st.session_state.new_docx = None

    # -------------------------------------------------------------
    # Show previous conversation
    # -------------------------------------------------------------

    for role, text in st.session_state.shown:

        with st.chat_message(role):

            if role == "assistant":
                st.markdown(
                    style_citations(text),
                    unsafe_allow_html=True,
                )

            else:
                st.markdown(text)

    # -------------------------------------------------------------
    # Chat input
    # -------------------------------------------------------------

    prompt = st.chat_input(
        "Ask a question, or say “draft an SOP about …”"
    )

    if prompt:

        st.session_state.shown.append(
            ("user", prompt)
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        before = _newest_docx_set()

        st.session_state.lc_messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        # ---------------------------------------------------------
        # ONLY NOW do we initialize the agent.
        #
        # This is the critical startup-performance improvement.
        # ---------------------------------------------------------

        with st.chat_message("assistant"):

            placeholder = st.empty()

            placeholder.markdown(
                "_Loading assistant…_"
            )

            answer = ""
            final_state = None

            try:

                agent = get_agent()

                placeholder.markdown(
                    "_Searching…_"
                )

                for mode, chunk in agent.stream(
                    {
                        "messages":
                            st.session_state.lc_messages
                    },
                    stream_mode=[
                        "messages",
                        "values",
                    ],
                ):

                    if mode == "messages":

                        msg, _meta = chunk

                        if isinstance(
                            msg,
                            AIMessageChunk,
                        ):

                            piece = _chunk_text(msg)

                            if piece:

                                answer += piece

                                placeholder.markdown(
                                    answer + " ▌"
                                )

                    elif mode == "values":

                        final_state = chunk

                placeholder.markdown(
                    style_citations(answer),
                    unsafe_allow_html=True,
                )

            except Exception as exc:

                answer = (
                    "I ran into an error while processing "
                    f"that request:\n\n`{exc}`"
                )

                placeholder.error(answer)

        if (
            final_state
            and final_state.get("messages")
        ):

            st.session_state.lc_messages = (
                final_state["messages"]
            )

        st.session_state.shown.append(
            ("assistant", answer)
        )

        # ---------------------------------------------------------
        # Detect newly generated Word file
        # ---------------------------------------------------------

        new_files = sorted(
            _newest_docx_set() - before
        )

        if new_files:

            st.session_state.new_docx = (
                new_files[-1]
            )

    # -------------------------------------------------------------
    # Newly generated SOP download
    # -------------------------------------------------------------

    new_docx = st.session_state.get(
        "new_docx"
    )

    if (
        new_docx
        and Path(new_docx).exists()
    ):

        path = Path(new_docx)

        st.divider()

        st.success(
            f"Draft ready: **{path.stem}**"
        )

        col1, col2 = st.columns(
            [1, 2]
        )

        with col1:

            st.download_button(
                "⬇️ Download Word (.docx)",
                path.read_bytes(),
                file_name=path.name,
                mime=_mime(path),
                type="primary",
                use_container_width=True,
            )

        with col2:

            st.caption(
                "Open **📄 SOP Library** to preview "
                "the document with its Word formatting."
            )


# =====================================================================
# SOP LIBRARY
# =====================================================================

else:

    st.subheader("📄 SOP Library")

    st.caption(
        "Browse your controlled documents. "
        "Documents are parsed only when you select one."
    )

    # -------------------------------------------------------------
    # Listing filenames is cheap.
    #
    # We do NOT call extract_text() for every document here.
    # -------------------------------------------------------------

    files = []

    for pattern in VIEWABLE:
        files.extend(
            SOPS_DIR.glob(pattern)
        )

    files = sorted(
        files,
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )

    if not files:

        st.info(
            "No documents in ./sops yet. "
            "Draft one from the Assistant, "
            "or add files and run `python ingest.py`."
        )

    else:

        # ---------------------------------------------------------
        # We know which document was freshly generated in this
        # Streamlit session without reopening every SOP.
        # ---------------------------------------------------------

        newest_draft = st.session_state.get(
            "new_docx"
        )

        draft_paths = set()

        if (
            newest_draft
            and Path(newest_draft).exists()
        ):

            draft_paths.add(
                str(Path(newest_draft))
            )

        left, right = st.columns(
            [1, 2],
            gap="large",
        )

        # ---------------------------------------------------------
        # Document list
        # ---------------------------------------------------------

        with left:

            only_drafts = st.checkbox(
                "Show drafts only",
                value=False,
            )

            if only_drafts:

                shown_files = [
                    path
                    for path in files
                    if str(path) in draft_paths
                ]

            else:

                shown_files = files

            if not shown_files:

                st.info(
                    "No generated drafts in this session."
                )

                selected = None

            else:

                choice = st.radio(
                    f"Documents ({len(shown_files)})",
                    options=range(
                        len(shown_files)
                    ),
                    format_func=lambda i: (
                        (
                            "🆕 "
                            if str(
                                shown_files[i]
                            )
                            in draft_paths
                            else ""
                        )
                        + (
                            f"{shown_files[i].stem}"
                            f" · "
                            f"{shown_files[i].suffix[1:]}"
                        )
                    ),
                )

                selected = (
                    shown_files[choice]
                )

        # ---------------------------------------------------------
        # Only the SELECTED document is parsed.
        # ---------------------------------------------------------

        with right:

            if selected:

                is_current_draft = (
                    str(selected)
                    in draft_paths
                )

                if is_current_draft:

                    st.markdown(
                        "<span class='draft-pill'>"
                        "DRAFT — pending QA"
                        "</span>",
                        unsafe_allow_html=True,
                    )

                suffix = (
                    selected.suffix.lower()
                )

                if suffix == ".docx":

                    with st.spinner(
                        "Opening document…"
                    ):

                        html_doc = doc_html(
                            str(selected),
                            selected.stat().st_mtime,
                        )

                    components.html(
                        html_doc,
                        height=780,
                        scrolling=True,
                    )

                else:

                    st.markdown(
                        f"### {selected.stem}"
                    )

                    with st.spinner(
                        "Opening document…"
                    ):

                        markdown_doc = (
                            doc_markdown(
                                str(selected),
                                selected.stat().st_mtime,
                            )
                        )

                    with st.container(
                        border=True
                    ):

                        st.markdown(
                            markdown_doc
                        )

                st.download_button(
                    "⬇️ Download this file",
                    selected.read_bytes(),
                    file_name=selected.name,
                    mime=_mime(selected),
                )
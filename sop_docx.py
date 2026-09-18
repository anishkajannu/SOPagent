"""Render a controlled SOP as a Word (.docx) document in Netramind house style.

Matches the real SOPs: NetraMind logo + bordered metadata header block on every
page, a bold Title line, numbered sections (1 Purpose … 6 Procedure) with hanging
indents, definition terms underlined, internal cross-references in red, a Revision
History table, and a Signature Page. Content comes in as the structured draft dict
the LLM produces; structure/numbering/formatting are fixed here.
"""

from __future__ import annotations

import datetime
import re
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

FONT = "Calibri"
SIZE = 11
GREY = "D9D9D9"
RED = RGBColor(0xC0, 0x00, 0x00)          # internal cross-reference color
LOGO_CANDIDATES = ["netramind_logo.png", "assets/netramind_logo.png"]

# A reference that points at another controlled document -> render in red.
_INTERNAL_REF = re.compile(r"^\s*(SOP|WIN|MAN|QM|POL|FRM|TMP|NM)\b", re.I)
# Strip a leading document number the model may have put in the title.
_TITLE_PREFIX = re.compile(r"^\s*(SOP|WIN|MAN|QM|POL)-\d{3}\s*[:\-–—]?\s*", re.I)


# ---------- low-level helpers ----------
def _font(run, size=SIZE, bold=False, italic=False, underline=False, color=None):
    run.font.name = FONT
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    run.underline = underline
    if color is not None:
        run.font.color.rgb = color
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs"):
        rfonts.set(qn(attr), FONT)


def _add_run(paragraph, text, **kw):
    r = paragraph.add_run(text)
    _font(r, **kw)
    return r


def _page_field(paragraph):
    def field(instr):
        r = paragraph.add_run()
        _font(r)
        begin = OxmlElement("w:fldChar"); begin.set(qn("w:fldCharType"), "begin")
        it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = instr
        end = OxmlElement("w:fldChar"); end.set(qn("w:fldCharType"), "end")
        r._r.append(begin); r._r.append(it); r._r.append(end)

    field("PAGE")
    _add_run(paragraph, " of ")
    field("NUMPAGES")


def _set_table_borders(table, color="000000", sz=4):
    tblPr = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement(f"w:{edge}")
        e.set(qn("w:val"), "single"); e.set(qn("w:sz"), str(sz))
        e.set(qn("w:space"), "0"); e.set(qn("w:color"), color)
        borders.append(e)
    tblPr.append(borders)


def _shade(cell, fill=GREY):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear"); shd.set(qn("w:fill"), fill)
    tcPr.append(shd)


def _cell_text(cell, text, bold=False, align=None, shade=False, size=SIZE):
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.space_before = Pt(1)
    if align is not None:
        p.alignment = align
    _add_run(p, text, bold=bold, size=size)
    if shade:
        _shade(cell)


def _find_logo(base: Path):
    for name in LOGO_CANDIDATES:
        p = base / name
        if p.exists():
            return p
    return None


# ---------- header / footer ----------
def _build_header(section, doc_number, title, version, effective, logo):
    header = section.header
    header.is_linked_to_previous = False
    outer = header.add_table(rows=1, cols=2, width=Inches(6.5))
    outer.autofit = False
    logo_cell, meta_cell = outer.rows[0].cells
    logo_cell.width = Inches(2.3); meta_cell.width = Inches(4.2)
    logo_cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER  # center against the table

    lp = logo_cell.paragraphs[0]
    if logo is not None:
        lp.add_run().add_picture(str(logo), width=Inches(2.4))
    else:
        _add_run(lp, "NetraMind", bold=True, size=16, color=RGBColor(0x1A, 0x56, 0xDB))

    meta = meta_cell.add_table(rows=5, cols=2)
    meta.autofit = False
    for row in meta.rows:
        row.cells[0].width = Inches(1.6); row.cells[1].width = Inches(2.5)
    _set_table_borders(meta)
    meta.rows[0].cells[0].merge(meta.rows[0].cells[1])
    _cell_text(meta.rows[0].cells[0], "STANDARD OPERATING PROCEDURE",
               align=WD_ALIGN_PARAGRAPH.CENTER, size=10)
    rows = [("Document Number:", doc_number), ("Effective Date:", effective),
            ("Version Number:", version), ("Page:", None)]
    for i, (label, value) in enumerate(rows, start=1):
        _cell_text(meta.rows[i].cells[0], label, align=WD_ALIGN_PARAGRAPH.RIGHT)
        if value is None:
            meta.rows[i].cells[1].text = ""
            _page_field(meta.rows[i].cells[1].paragraphs[0])
        else:
            _cell_text(meta.rows[i].cells[1], value)

    tp = header.add_paragraph()
    _add_run(tp, "Title: ", bold=True)
    _add_run(tp, title, bold=True)


def _build_footer(section):
    footer = section.footer
    footer.is_linked_to_previous = False
    p1 = footer.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _add_run(p1, "THIS DOCUMENT CONTAINS CONFIDENTIAL AND PROPRIETARY INFORMATION", size=9)
    p2 = footer.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.RIGHT   # page number on the right, like the official SOPs
    _add_run(p2, "Page ")                     # default black Calibri, same as the body
    _page_field(p2)


# ---------- body ----------
def _section_heading(doc, num, title):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.tab_stops.add_tab_stop(Inches(0.35))  # small gap: "1  PURPOSE"
    _add_run(p, str(num), bold=True)
    _add_run(p, "\t", bold=True)
    _add_run(p, title, bold=True)


def _body(doc, text):
    """A plain indented body paragraph (Purpose, Scope) aligned under the heading word."""
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.35)
    p.paragraph_format.space_after = Pt(6)
    _add_run(p, text)


def _num_clause(doc, label, text, level=0):
    """A numbered clause (5.1, 6.1, …) with a hanging indent."""
    left = 0.9 + level * 0.4
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(left)
    p.paragraph_format.first_line_indent = Inches(-0.4)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.tab_stops.add_tab_stop(Inches(left))  # text aligns with wrapped lines
    _add_run(p, f"{label}\t")
    _add_run(p, text)


def _definition(doc, label, text):
    """A definition line with the term underlined, like the real SOPs."""
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.9)
    p.paragraph_format.first_line_indent = Inches(-0.4)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.tab_stops.add_tab_stop(Inches(0.9))
    _add_run(p, f"{label}\t")
    term, sep, rest = text.partition("—")   # em dash
    if not sep:
        term, sep, rest = text.partition(" - ")
    if sep:
        _add_run(p, term.strip(), underline=True)
        _add_run(p, " — ")
        _add_run(p, rest.strip())
    else:
        _add_run(p, text)


def _render_hier(doc, items, major):
    """Render a section (5=Responsibilities, 6=Procedure) with sub-subsections.

    Each item may be a plain string (renders as `major.i`) or a dict with a
    heading (`role`/`step`) plus a list of sub-items (`duties`/`substeps`),
    which render as `major.i.j`.
    """
    for i, item in enumerate(items or ["[None]"], start=1):
        if isinstance(item, dict):
            head = (item.get("role") or item.get("step") or "").strip()
            subs = item.get("duties") or item.get("substeps") or []
            _num_clause(doc, f"{major}.{i}", head)
            for j, sub in enumerate(subs, start=1):
                _num_clause(doc, f"{major}.{i}.{j}", str(sub).strip(), level=1)
        else:
            _num_clause(doc, f"{major}.{i}", str(item).strip())


def _reference(doc, text):
    """A reference bullet; internal document references render in red."""
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.9)
    p.paragraph_format.first_line_indent = Inches(-0.4)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.tab_stops.add_tab_stop(Inches(0.9))
    _add_run(p, "•\t")
    _add_run(p, text, color=RED if _INTERNAL_REF.match(text) else None)


def _clean_title(title: str) -> str:
    title = re.sub(r"^\s*title\s*:\s*", "", title, flags=re.I)
    title = _TITLE_PREFIX.sub("", title)
    return title.strip()


def build_sop_docx(doc_number, draft, out_path, base_dir=".", version="01", effective="[On approval]"):
    base = Path(base_dir)
    doc = Document()

    normal = doc.styles["Normal"]
    normal.font.name = FONT
    normal.font.size = Pt(SIZE)

    sec = doc.sections[0]
    sec.page_width = Inches(8.5); sec.page_height = Inches(11)
    sec.left_margin = Inches(1); sec.right_margin = Inches(1)
    sec.top_margin = Inches(1.6); sec.bottom_margin = Inches(0.9)

    title = _clean_title(draft.get("title", "").strip())
    _build_header(sec, doc_number, title, version, effective, _find_logo(base))
    _build_footer(sec)

    _section_heading(doc, 1, "PURPOSE")
    _body(doc, draft.get("purpose", "").strip())

    _section_heading(doc, 2, "SCOPE")
    _body(doc, draft.get("scope", "").strip())

    _section_heading(doc, 3, "REFERENCES")
    for ref in draft.get("references", []) or ["[None]"]:
        _reference(doc, ref.strip())

    _section_heading(doc, 4, "DEFINITIONS")
    for i, d in enumerate(draft.get("definitions", []) or ["[None]"], start=1):
        _definition(doc, f"4.{i}", d.strip())

    _section_heading(doc, 5, "RESPONSIBILITIES")
    _render_hier(doc, draft.get("responsibilities", []), 5)

    _section_heading(doc, 6, "PROCEDURE")
    _render_hier(doc, draft.get("procedure", []), 6)

    rp = doc.add_paragraph(); rp.paragraph_format.space_before = Pt(12)
    _add_run(rp, "REVISION HISTORY", bold=True)
    rev = doc.add_table(rows=2, cols=3); _set_table_borders(rev)
    for c, h in zip(rev.rows[0].cells, ("Version Number", "Date", "Summary of Change(s)")):
        _cell_text(c, h, bold=True, shade=True, align=WD_ALIGN_PARAGRAPH.CENTER)
    today = datetime.date.today().strftime("%d-%b-%Y").upper()   # e.g. 18-SEP-2026
    row = rev.rows[1].cells
    _cell_text(row[0], version, align=WD_ALIGN_PARAGRAPH.CENTER)
    _cell_text(row[1], today, align=WD_ALIGN_PARAGRAPH.CENTER)
    _cell_text(row[2], "Initial draft (pending QA approval)")

    doc.add_page_break()
    sp = doc.add_paragraph(); _add_run(sp, "SIGNATURE PAGE", bold=True)
    _add_run(doc.add_paragraph(), "[ADD ADDITIONAL ROWS AS NEEDED]")
    for role in ("Author", "Reviewer", "Approver"):
        rlp = doc.add_paragraph(); rlp.paragraph_format.space_before = Pt(8)
        _add_run(rlp, role + ":")
        t = doc.add_table(rows=2, cols=4); _set_table_borders(t)
        for c, h in zip(t.rows[0].cells, ("NAME", "TITLE", "SIGNATURE", "DATE")):
            _cell_text(c, h, bold=True, shade=True)
        for c in t.rows[1].cells:
            _cell_text(c, " ")

    doc.save(str(out_path))
    return str(out_path)

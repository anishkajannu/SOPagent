"""Convert the markdown SOPs in ./sops into house-style .docx documents.

Faithfully preserves each document's real content (every section, in order),
rendered in the Netramind house style (logo + metadata header, numbered section
headings, hanging-indent clauses, underlined definition terms, red internal
references). Reuses the renderers in sop_docx.py so it matches generated SOPs.

Usage:
  python md2docx.py one "SOP-005 Management Review Meetings.md"   # convert one (no archive)
  python md2docx.py                                                # convert all, archive the .md
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

from docx import Document
from docx.shared import Inches, Pt

import sop_docx as S

SOPS = Path("./sops")
ARCHIVE = SOPS / "_archive"

_TITLE = re.compile(r"^#\s*(.+?)\s*$")
_DOCNUM_IN_TITLE = re.compile(r"^([A-Z]{2,}(?:-[A-Z0-9]+)+(?:-v[\d.]+)?)\s*[—–\-:]\s*(.*)$")
# A top-level section heading: "1 PURPOSE", "1. PURPOSE", "8 REVISION HISTORY".
_MAJOR = re.compile(r"^(\d+)\.?\s+([A-Z][A-Z0-9 /&()\-.]*[A-Z)])\s*$")
# A numbered clause: "4.1 …", "5.1.1 …", "6.2.2 …".
_CLAUSE = re.compile(r"^(\d+(?:\.\d+)+)\.?\s+(.*)$")
_BULLET = re.compile(r"^[•▪◦·\-*]\s+(.*)$")
_REVROW = re.compile(r"\b(\d{2})\s+(\d{1,2}-[A-Za-z]{3}-\d{4})\b")


def parse(md: str):
    """Return (doc_number, title, [ [kind, label, text], … ]) preserving order."""
    lines = md.split("\n")
    doc_number, title, start = "", "", 0
    if lines and lines[0].lstrip().startswith("#"):
        t = _TITLE.match(lines[0]).group(1)
        dm = _DOCNUM_IN_TITLE.match(t)
        doc_number, title = (dm.group(1), dm.group(2).strip()) if dm else ("", t.strip())
        start = 1

    elements: list[list] = []
    cur = None
    for raw in lines[start:]:
        s = raw.strip()
        if not s:
            cur = None
            continue
        mm = _MAJOR.match(s)
        if mm and not _CLAUSE.match(s):
            elements.append(["major", mm.group(1), mm.group(2).strip()])
            cur = None
            continue
        cm = _CLAUSE.match(s)
        if cm:
            elements.append(["clause", cm.group(1), cm.group(2).strip()])
            cur = elements[-1]
            continue
        bm = _BULLET.match(s)
        if bm:
            elements.append(["bullet", None, bm.group(1).strip()])
            cur = elements[-1]
            continue
        # otherwise: continuation of the previous wrapped line, or a new paragraph
        if cur and cur[0] in ("clause", "bullet", "plain"):
            cur[2] = (cur[2] + " " + s).strip()
        else:
            elements.append(["plain", None, s])
            cur = elements[-1]
    return doc_number, title, elements


def _meta(md: str):
    m = _REVROW.search(md)
    return (m.group(1), m.group(2).upper()) if m else ("01", "[On approval]")


def build(md: str, out_path: Path, base_dir: str = ".") -> None:
    doc_number, title, elements = parse(md)
    version, effective = _meta(md)

    doc = Document()
    normal = doc.styles["Normal"]
    normal.font.name = S.FONT
    normal.font.size = Pt(S.SIZE)

    sec = doc.sections[0]
    sec.page_width = Inches(8.5); sec.page_height = Inches(11)
    sec.left_margin = Inches(1); sec.right_margin = Inches(1)
    sec.top_margin = Inches(1.6); sec.bottom_margin = Inches(0.9)

    S._build_header(sec, doc_number, S._clean_title(title), version, effective,
                    S._find_logo(Path(base_dir)))
    S._build_footer(sec)

    current = ""
    for kind, label, text in elements:
        if kind == "major":
            current = text.upper()
            S._section_heading(doc, label, text.upper())
        elif kind == "clause":
            if "DEFINITION" in current:
                S._definition(doc, label, text)
            else:
                S._num_clause(doc, label, text, level=max(0, label.count(".") - 1))
        elif kind == "bullet":
            S._reference(doc, text)          # reddens internal doc refs, plain otherwise
        else:
            S._body(doc, text)

    doc.save(str(out_path))


def main() -> None:
    ARCHIVE.mkdir(exist_ok=True)
    converted, already_docx, failed = [], [], []
    for md in sorted(SOPS.glob("*.md")):
        docx_path = md.with_suffix(".docx")
        try:
            if docx_path.exists():
                # A .docx for this document already exists (e.g. an uploaded version) —
                # keep it, just retire the markdown copy.
                shutil.move(str(md), str(ARCHIVE / md.name))
                already_docx.append(md.name)
                continue
            build(md.read_text(encoding="utf-8", errors="ignore"), docx_path)
            shutil.move(str(md), str(ARCHIVE / md.name))
            converted.append(md.name)
        except Exception as e:
            failed.append(f"{md.name}: {e}")

    print(f"CONVERTED {len(converted)} .md -> .docx")
    for c in converted:
        print("  +", c)
    if already_docx:
        print(f"ARCHIVED (a .docx already existed): {len(already_docx)}")
        for c in already_docx:
            print("  =", c)
    if failed:
        print(f"FAILED: {len(failed)}")
        for f in failed:
            print("  !", f)


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "one":
        target = SOPS / sys.argv[2]
        build(target.read_text(encoding="utf-8", errors="ignore"), target.with_suffix(".docx"))
        print("built", target.with_suffix(".docx").name)
    else:
        main()

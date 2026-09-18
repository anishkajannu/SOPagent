"""Controlled SOP template for generated SOPs.

The template mirrors the structure of Netramind's existing SOPs in ./sops:
numbered H2 sections and a Revision History table. The structure, the section
numbering, and the document number are FIXED here (deterministic code); the
LLM only supplies the prose that fills the {fields}. This is what keeps every
generated SOP consistent and compliant.
"""

# Order the model must return content for. Matches the existing markdown SOPs.
SECTION_ORDER = ["purpose", "scope", "responsibilities", "procedure", "references"]

# {fields} are filled by generate.py; headings/numbers are never model output.
SOP_TEMPLATE = """# {doc_number} — {title}

## 1. Purpose
{purpose}

## 2. Scope
{scope}

## 3. Responsibilities
{responsibilities}

## 4. Procedure
{procedure}

## 5. References
{references}

## 6. Revision History
| Version | Date | Change |
|---|---|---|
| {version} | {date} | {change} |
"""


def bullet_list(items: list[str]) -> str:
    """Render a list of strings as markdown bullets (for Responsibilities/References)."""
    items = [i.strip() for i in items if i and i.strip()]
    return "\n".join(f"- {i}" for i in items) if items else "- [To be completed]"


def numbered_list(items: list[str]) -> str:
    """Render a list of strings as a markdown numbered list (for Procedure)."""
    items = [i.strip() for i in items if i and i.strip()]
    return "\n".join(f"{n}. {i}" for n, i in enumerate(items, 1)) if items else "1. [To be completed]"

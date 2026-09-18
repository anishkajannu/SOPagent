
from pathlib import Path

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_chroma import Chroma
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from generate import generate_sop
from gov import search_government_policy
from ingest import load_doc, build_stable_ids


embeddings = FastEmbedEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


sop_store = Chroma(
    collection_name="netramind_sops",
    embedding_function=embeddings,
    persist_directory="./chroma_sops",
)


@tool
def search_sops(query: str) -> str:
    """Search internal Netramind SOPs for information relevant to a user's question."""

    hits = sop_store.similarity_search(query, k=3)

    if not hits:
        return "No matching SOP information was found."

    results = []

    for document in hits:
        doc_number = document.metadata.get("doc_number", "UNKNOWN")
        title = document.metadata.get("title", "Unknown title")
        text = document.page_content

        results.append(
            f"[{doc_number} — {title}]\n{text}"
        )

    return "\n\n---\n\n".join(results)


def _index_file(path: Path) -> None:
    """Add a single new/updated document file to the search index immediately."""
    doc = load_doc(path)
    splitter = RecursiveCharacterTextSplitter(
        separators=["\n## ", "\n### ", "\n\n", "\n", " "],
        chunk_size=800,
        chunk_overlap=120,
    )
    chunks = splitter.split_documents([doc])
    sop_store.add_documents(chunks, ids=build_stable_ids(chunks))


@tool
def draft_sop(topic: str, doc_type: str = "SOP") -> str:
    """Draft a NEW controlled document from the Netramind template.

    Use this when the user asks to create, generate, or draft a new SOP.
    The document number (e.g. SOP-033) is assigned automatically as the next
    number in the series, so you do NOT need any codes from the user.
    `doc_type` is the series to number within (SOP, WIN, POL, MAN, QM);
    default "SOP". The result is a DRAFT for author/QA review, not an
    approved document.
    """

    result = generate_sop(
        topic=topic,
        doc_type=doc_type,
    )

    # Make the new draft searchable right away — no separate ingest step needed.
    try:
        _index_file(Path(result["path"]))
        indexed = "It is already indexed, so you can ask about it now."
    except Exception as e:
        indexed = f"(Could not auto-index it: {e}. Run `python ingest.py` to index it.)"

    return (
        f"Drafted {result['doc_number']} — {result['title']}\n"
        f"Saved to: {result['path']}\n"
        f"{indexed}\n"
        "This is a DRAFT for author/QA review and approval before use."
    )


@tool
def gov_policy(query: str) -> str:
    """Look up external GOVERNMENT / regulatory policy from official sources only.

    Use this (not search_sops) when the user asks about laws, regulations, or
    government guidance such as FDA, EMA, ICH, or 21 CFR — anything outside
    Netramind's own procedures. Returns passages with their official source URL
    and the date retrieved.
    """

    return search_government_policy(query)


agent = create_agent(
    model="anthropic:claude-sonnet-5",
    tools=[search_sops, draft_sop, gov_policy],
    system_prompt=(
        "You are Netramind's SOP assistant.\n"
        "- For questions about Netramind's own procedures or policies, use the "
        "search_sops tool before answering, only make claims supported by the "
        "retrieved SOP content, and always cite the SOP document number.\n"
        "- For questions about external laws, regulations, or government guidance "
        "(e.g. FDA, EMA, ICH, 21 CFR), use the gov_policy tool. Only state "
        "regulatory facts that are supported by a retrieved official source, and "
        "cite that source's URL and retrieved date. Never answer a regulatory "
        "question from memory; if no official source is returned, say you cannot "
        "confirm it from an authoritative source. Keep internal SOP content and "
        "external regulation clearly separate, and never present one as the other.\n"
        "- When the user asks to create, generate, or draft a new SOP, use the "
        "draft_sop tool. The document number is assigned automatically (e.g. "
        "SOP-033), so you do not need department or category codes — just draft it "
        "from the topic. Remind the user that generated SOPs are drafts that still "
        "require author and QA review and approval before use.\n"
        "- If you do not have the answer from a tool, say so rather than guessing."
    ),
)


def main():
    print("Netramind SOP assistant. Ask a question, or type 'quit' to exit.\n")

    messages = []  # keeps the whole conversation so follow-ups have context

    while True:
        try:
            question = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break

        if question.lower() in {"quit", "exit", "q", ""}:
            print("Goodbye.")
            break

        messages.append({"role": "user", "content": question})

        response = agent.invoke({"messages": messages})
        messages = response["messages"]  # carry full history (incl. tool calls) forward

        last = messages[-1]
        answer = getattr(last, "text", None) or getattr(last, "content", "")
        print(f"\nAssistant: {answer}\n")


if __name__ == "__main__":
    main()

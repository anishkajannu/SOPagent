"""Government / official policy advisor — LIVE search, official sources only.

You ask a plain-language policy question; this searches official government
sites in real time and returns the matching passages with their source URLs,
so you never need to know which CFR part or guidance it lives in.

The "government only" rule is enforced in CODE, two ways:
  1. the search is restricted to the allow-listed domains at query time, and
  2. every returned result is re-checked against the allow-list before use.

Requires a Tavily API key (free tier available at https://tavily.com):
set it in your environment as  TAVILY_API_KEY=...
"""

from __future__ import annotations

import datetime
import os
from urllib.parse import urlparse

# ---- The enforcement point: only these official domains are ever consulted. ----
# Suffix match, so "www.fda.gov" and "open.fda.gov" both match "fda.gov".
ALLOWED_DOMAINS = {
    "fda.gov",
    "ecfr.gov",
    "federalregister.gov",
    "ema.europa.eu",
    "ich.org",
    "who.int",
    "mhra.gov.uk",
    "hhs.gov",
}


def is_allowed(url: str) -> bool:
    """True only if the URL's host is (a subdomain of) an allow-listed official domain."""
    host = (urlparse(url).hostname or "").lower()
    return any(host == d or host.endswith("." + d) for d in ALLOWED_DOMAINS)


def search_government_policy(query: str, max_results: int = 5) -> str:
    """Search official GOVERNMENT / regulatory sources live and return cited passages.

    Use for any question about external laws, regulations, or government guidance
    (e.g. FDA, EMA, ICH, 21 CFR) — even when you don't know which rule it is. The
    search is limited to official domains; results carry their source URL and the
    date retrieved. Kept separate from internal Netramind SOPs.
    """
    if not os.environ.get("TAVILY_API_KEY"):
        return (
            "Government search is not configured: set the TAVILY_API_KEY environment "
            "variable (free key at https://tavily.com) so I can look up official sources."
        )

    try:
        from langchain_tavily import TavilySearch  # requires `pip install langchain-tavily`
    except ImportError:
        return (
            "The langchain-tavily package is not installed. "
            "Run `pip install langchain-tavily` to enable live government search."
        )

    search = TavilySearch(
        max_results=max_results,
        include_domains=sorted(ALLOWED_DOMAINS),  # restrict the search itself
        search_depth="advanced",
    )

    try:
        response = search.invoke({"query": query})
    except Exception as e:  # network/auth/rate-limit
        return f"Could not reach the government search service right now ({e})."

    # Response is usually {"results": [{"title","url","content",...}, ...]}.
    results = response.get("results", []) if isinstance(response, dict) else response
    today = datetime.date.today().isoformat()

    blocks = []
    for r in results:
        url = (r.get("url") or "").strip()
        if not is_allowed(url):  # belt-and-suspenders: drop anything off the allow-list
            continue
        title = r.get("title") or url
        content = (r.get("content") or "").strip()
        blocks.append(f"[Official source: {title} — {url} — retrieved {today}]\n{content}")

    if not blocks:
        return (
            "No official government source was found for that. I only consult official "
            "sources, so I can't confirm it from an authoritative source right now."
        )
    return "\n\n---\n\n".join(blocks)


if __name__ == "__main__":
    q = input("Ask about a government / regulatory policy: ")
    print("\n" + search_government_policy(q))

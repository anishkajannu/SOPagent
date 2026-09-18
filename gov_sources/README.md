# Government / policy advisor (live search)

The `gov_policy` tool answers plain-language policy questions by searching
**official government sites in real time** — you don't need to know which CFR
part or guidance document the answer lives in. It searches only the allow-listed
domains and cites each source with the date retrieved.

## Allowed domains (edit in gov.py -> ALLOWED_DOMAINS)
fda.gov · ecfr.gov · federalregister.gov · ema.europa.eu · ich.org · who.int ·
mhra.gov.uk · hhs.gov

## One-time setup
1. Get a free Tavily API key at https://tavily.com
2. Install the package:  `pip install langchain-tavily`  (already in requirements.txt)
3. Set the key in your environment before running:

   ```
   export TAVILY_API_KEY="tvly-your-key-here"     # macOS/Linux
   ```

That's it — no documents to load. Then run `python main.py` and ask a policy
question, e.g. *"Can we use electronic signatures instead of wet-ink for batch
records?"*  The advisor will search official sources, answer, and cite the URLs.

## Note
`21-CFR-Part-11.md` in this folder is just a bundled offline reference copy of
that regulation; live search does not require it and does not read it.

## Keeping it trustworthy
The advisor *surfaces and cites* official text with a retrieval date — QA still
makes the final compliance determination. To broaden or narrow what it will
consult, edit `ALLOWED_DOMAINS` in `gov.py`.

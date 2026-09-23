# Netramind SOP Assistant — Run It Locally

A short guide to running the SOP Assistant on your own computer to test it.
You have two options: **Docker** (simplest — one command, nothing to install but Docker)
or **Python** (if you'd rather not use Docker). Pick whichever you prefer.

Either way you'll open the app at **http://localhost:8000** in your browser.

---

## Before you start (both options)

1. **Get access to the code.** The project lives at
   `https://github.com/anishkajannu/SOPagent`. If it's private, ask Shailesh to
   add your GitHub username as a collaborator so you can clone it.

2. **Get an Anthropic API key.** The assistant uses Claude, so you need a key.
   Get one at <https://console.anthropic.com> → **API Keys** → *Create Key*.
   It looks like `sk-ant-...`. (Optional: a Tavily key from <https://tavily.com>
   enables the live government-regulation lookup. Everything else works without it.)

   > ⚠️ Keep your key private — don't paste it into the code or commit it. You'll
   > pass it in when you start the app, as shown below.

3. **Install git** if you don't have it: <https://git-scm.com/downloads>.

---

## Option A — Docker (recommended)

Easiest and most reliable: it bundles everything (Python, the search index, the
embedding model) so nothing else needs setting up.

1. **Install Docker Desktop** if you don't have it: <https://www.docker.com/products/docker-desktop/>.
   Open it once so it's running (you'll see the whale icon in your menu bar / taskbar).

2. **Clone the repo** — open Terminal (Mac) or PowerShell (Windows) and run:
   ```bash
   git clone https://github.com/anishkajannu/SOPagent.git
   cd SOPagent
   ```

3. **Build the image** (first time takes a few minutes):
   ```bash
   docker build -t netramind-sop .
   ```

4. **Run it**, pasting in your Anthropic key:

   **Mac / Linux:**
   ```bash
   docker run -p 8000:8000 -e ANTHROPIC_API_KEY=sk-ant-YOURKEY netramind-sop
   ```
   **Windows (PowerShell):**
   ```powershell
   docker run -p 8000:8000 -e ANTHROPIC_API_KEY=sk-ant-YOURKEY netramind-sop
   ```
   (To also enable the regulation lookup, add `-e TAVILY_API_KEY=tvly-YOURKEY`.)

5. **Open the app:** go to <http://localhost:8000> in your browser.

6. **To stop it:** press `Ctrl+C` in the terminal window.

---

## Option B — Python (no Docker)

Use this if you'd rather not install Docker. You'll need **Python 3.10 or newer**
(<https://www.python.org/downloads/>).

1. **Clone the repo:**
   ```bash
   git clone https://github.com/anishkajannu/SOPagent.git
   cd SOPagent
   ```

2. **Create and activate a virtual environment:**

   **Mac / Linux:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
   **Windows (PowerShell):**
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your Anthropic API key** in the same terminal:

   **Mac / Linux:**
   ```bash
   export ANTHROPIC_API_KEY=sk-ant-YOURKEY
   # optional: export TAVILY_API_KEY=tvly-YOURKEY
   ```
   **Windows (PowerShell):**
   ```powershell
   $env:ANTHROPIC_API_KEY = "sk-ant-YOURKEY"
   # optional: $env:TAVILY_API_KEY = "tvly-YOURKEY"
   ```

5. **Start the app:**
   ```bash
   uvicorn server:app --port 8000
   ```

6. **Open the app:** go to <http://localhost:8000>.

7. **To stop it:** press `Ctrl+C` in the terminal.

> The very first question may take a few extra seconds — the app downloads a small
> (~90 MB) embedding model the first time, then it's fast after that.

---

## Trying it out

- **Ask about an existing SOP:** e.g. *"What does our audit trail review SOP cover?"*
- **Draft a new one:** e.g. *"Draft an SOP about equipment cleaning."* When it
  finishes, a green **Download Word (.docx)** card appears right in the chat, and
  the draft shows up in the **SOP Library** tab with full formatting.
- **Ask a regulation question** (needs the Tavily key): e.g. *"What does 21 CFR
  Part 11 require for electronic signatures?"*

Drafts you generate are saved into the `sops/` folder on your own computer and
stay there. (They are drafts for review — they still need author/QA approval.)

---

## Updating the SOPs (the **Manage** tab)

When SOPs change, you don't need to touch any files by hand or re-send anything to
anyone — do it all in the **🔧 Manage** tab:

1. **Upload** the new or changed `.docx` / `.pdf` / `.md` files. A file with the same
   name replaces the old version.
2. **Archive** any SOP that's now obsolete (click *Archive* next to it). It moves to
   `sops/_archive` — kept on disk for your records, but the assistant stops using it.
3. Click **🔄 Rebuild index now.** This wipes the old index and re-reads only the
   current SOPs, so anything you removed can no longer be recalled. When it finishes,
   it shows exactly which documents are now indexed and the date/time — that list is
   your record of what the assistant is running on.

Always **Rebuild** after uploading or archiving — that's the step that actually applies
your changes.

---

## If something goes wrong

- **"port already in use"** — something else is on 8000. Use another port, e.g.
  `uvicorn server:app --port 8010` (or `-p 8010:8000` for Docker), then open
  `http://localhost:8010`.
- **The assistant errors on the first question** — usually the API key isn't set.
  Make sure you set `ANTHROPIC_API_KEY` in the *same* terminal you started the app
  in, and that the key is valid.
- **The page loads but the SOP Library is empty** — you're likely running from the
  wrong folder; make sure you're inside the `SOPagent` folder when you start it.
- **Still stuck?** Send Shailesh the last few lines the terminal printed.

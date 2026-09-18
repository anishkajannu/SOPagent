# Deploying the Netramind SOP Assistant with Docker

This packages the whole app — code, your SOP index, the local embedding model — into
one image that runs the same anywhere. Your API keys are **not** baked in; they're
passed at run time.

> Keep this image internal (a private registry or an internal server). It contains
> your SOP content, so do not push it to a public registry like Docker Hub.

## 1. One-time: install Docker
Install **Docker Desktop** (Mac/Windows) or Docker Engine (Linux).

## 2. Build the image
From the project folder (`~/langchain-quickstart`):

```
docker build -t netramind-sop .
```

This installs dependencies, downloads the embedding model into the image, and builds
the SOP search index from `./sops`. First build takes a few minutes.

## 3. Run it (locally, to test)
Pass your two keys at run time:

```
docker run -p 8501:8501 \
  -e ANTHROPIC_API_KEY="sk-ant-…" \
  -e TAVILY_API_KEY="tvly-…" \
  netramind-sop
```

Open http://localhost:8501.

## 4. Share it with the team
Pick one:

**A. Run it on an internal server / VM (recommended).**
Put the image on a machine your team can reach (behind the company VPN):
- Copy the project there and `docker build`, **or** ship the image directly:
  ```
  docker save netramind-sop | gzip > netramind-sop.tar.gz     # on your Mac
  # copy the file to the server, then on the server:
  docker load < netramind-sop.tar.gz
  ```
- Start it so it stays up and restarts automatically:
  ```
  docker run -d --restart unless-stopped -p 8501:8501 \
    -e ANTHROPIC_API_KEY="sk-ant-…" \
    -e TAVILY_API_KEY="tvly-…" \
    --name netramind-sop netramind-sop
  ```
- Team members visit `http://<server-address>:8501`.

**B. Quick shared demo (no server).**
Run the container on your Mac (step 3), then expose it temporarily:
```
brew install cloudflared
cloudflared tunnel --url http://localhost:8501
```
It prints a public `https://…trycloudflare.com` link. Only up while your Mac + the
tunnel run, and anyone with the link can use it — good for a live demo, not permanent.

## 5. Keeping SOPs current
The index is built into the image, so after you add or edit SOPs, **rebuild** to pick
them up:
```
docker build -t netramind-sop .
```
(Then restart the container.) If you'd rather update SOPs without rebuilding, mount a
live folder instead — ask and I'll wire that up.

## Notes on access & security
- **Keys:** never bake keys into the image; always pass them with `-e` (or an
  `--env-file`). Rotate them if a container host is shared.
- **Login:** the app itself has no authentication. For anything beyond a trusted
  internal network, put it behind a reverse proxy (nginx/Caddy) with basic auth or your
  company SSO. I can set that up if you want.
- **Compliance:** this is a drafting/lookup aid, not validated software — generated SOPs
  remain drafts pending author/QA approval.

"use strict";

// ---- session id (server keeps conversation memory keyed by this) ----
let SESSION_ID = localStorage.getItem("nm_session");
if (!SESSION_ID) {
  SESSION_ID = (crypto.randomUUID ? crypto.randomUUID() : String(Math.random()).slice(2));
  localStorage.setItem("nm_session", SESSION_ID);
}

const GOV_DOMAINS = ["fda.gov", "ecfr.gov", "federalregister.gov", "ema.europa.eu",
                     "ich.org", "who.int", "mhra.gov.uk", "hhs.gov"];
const DOCNUM_RE = /\b((?:SOP|WIN|MAN|QM|POL|FRM|TMP|NM)-\d{3}(?:-\d{2})?)\b/g;

let agentReady = false;

// ---------------- tabs ----------------
document.querySelectorAll(".tab").forEach((btn) => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".tab").forEach((b) => b.classList.remove("active"));
    document.querySelectorAll(".tabpane").forEach((p) => p.classList.remove("active"));
    btn.classList.add("active");
    document.getElementById(btn.dataset.tab).classList.add("active");
    if (btn.dataset.tab === "library") loadLibrary();
    if (btn.dataset.tab === "manage") loadManage();
  });
});

// ---------------- citation styling ----------------
function isGov(host) {
  host = host.replace(/^www\./, "").toLowerCase();
  return GOV_DOMAINS.some((d) => host === d || host.endsWith("." + d));
}

function styleCitations(rootEl) {
  // Official-source links -> blue pills.
  rootEl.querySelectorAll("a[href]").forEach((a) => {
    try {
      if (isGov(new URL(a.href).hostname)) {
        a.classList.add("cite-gov");
        a.target = "_blank";
        if (!a.dataset.pilled) { a.textContent = "🏛️ " + a.textContent; a.dataset.pilled = "1"; }
      }
    } catch (e) { /* ignore bad URLs */ }
  });
  // SOP doc numbers in plain text -> green pills (skip links/code).
  const walker = document.createTreeWalker(rootEl, NodeFilter.SHOW_TEXT, {
    acceptNode(node) {
      if (!node.nodeValue || !/[A-Z]{2,3}-\d{3}/.test(node.nodeValue)) return NodeFilter.FILTER_REJECT;
      let p = node.parentElement;
      while (p && p !== rootEl) {
        const t = p.tagName;
        if (t === "A" || t === "CODE" || t === "PRE") return NodeFilter.FILTER_REJECT;
        p = p.parentElement;
      }
      return NodeFilter.FILTER_ACCEPT;
    },
  });
  const targets = [];
  while (walker.nextNode()) targets.push(walker.currentNode);
  targets.forEach((node) => {
    const frag = document.createDocumentFragment();
    let last = 0;
    const text = node.nodeValue;
    text.replace(DOCNUM_RE, (match, _g, idx) => {
      if (idx > last) frag.appendChild(document.createTextNode(text.slice(last, idx)));
      const span = document.createElement("span");
      span.className = "cite-sop";
      span.textContent = "📘 " + match;
      frag.appendChild(span);
      last = idx + match.length;
      return match;
    });
    if (last < text.length) frag.appendChild(document.createTextNode(text.slice(last)));
    node.parentNode.replaceChild(frag, node);
  });
}

function renderMarkdown(el, text) {
  el.innerHTML = window.marked ? window.marked.parse(text) : text.replace(/\n/g, "<br>");
  styleCitations(el);
}

// ---------------- chat ----------------
const chatEl = document.getElementById("chat");
const formEl = document.getElementById("chat-form");
const inputEl = document.getElementById("chat-input");
const sendBtn = document.getElementById("send-btn");

function resetChat() {
  // Clear the visible conversation and start a fresh server-side session.
  chatEl.innerHTML = "";
  SESSION_ID = (crypto.randomUUID ? crypto.randomUUID() : String(Math.random()).slice(2));
  try { localStorage.setItem("nm_session", SESSION_ID); } catch (e) {}
}

function addBubble(role) {
  const wrap = document.createElement("div");
  wrap.className = "msg " + role;
  const bubble = document.createElement("div");
  bubble.className = "bubble";
  wrap.appendChild(bubble);
  chatEl.appendChild(wrap);
  chatEl.scrollTop = chatEl.scrollHeight;
  return bubble;
}

fetch("/api/ready").then((r) => r.json()).then((d) => { agentReady = !!d.ready; }).catch(() => {});

formEl.addEventListener("submit", async (e) => {
  e.preventDefault();
  const message = inputEl.value.trim();
  if (!message) return;
  inputEl.value = "";
  sendBtn.disabled = true;

  addBubble("user").textContent = message;

  const bubble = addBubble("assistant");
  bubble.innerHTML = `<span class="status">${agentReady ? "Thinking…" : "Waking up assistant…"}</span>`;

  let answer = "";
  let firstToken = true;
  try {
    const resp = await fetch("/api/chat/stream", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message, session_id: SESSION_ID }),
    });
    if (!resp.ok || !resp.body) throw new Error("Request failed (" + resp.status + ")");

    const reader = resp.body.getReader();
    const decoder = new TextDecoder();
    let buffer = "";

    while (true) {
      const { value, done } = await reader.read();
      if (done) break;
      buffer += decoder.decode(value, { stream: true });
      let nl;
      while ((nl = buffer.indexOf("\n")) >= 0) {
        const line = buffer.slice(0, nl).trim();
        buffer = buffer.slice(nl + 1);
        if (!line) continue;
        let obj;
        try { obj = JSON.parse(line); } catch (e) { continue; }

        if (obj.error) {
          bubble.innerHTML = `<span class="status">⚠️ ${obj.error}</span>`;
        } else if (obj.delta) {
          if (firstToken) { bubble.textContent = ""; agentReady = true; firstToken = false; }
          answer += obj.delta;
          bubble.textContent = answer;            // stream as plain text
          bubble.innerHTML = escapeHtml(answer) + '<span class="cursor">▌</span>';
          chatEl.scrollTop = chatEl.scrollHeight;
        } else if (obj.done) {
          renderMarkdown(bubble, answer);         // finalize: markdown + pills
          if (obj.new_docx) showDraft(obj.new_docx);
        }
      }
    }
    if (answer && bubble.querySelector(".cursor")) renderMarkdown(bubble, answer);
  } catch (err) {
    bubble.innerHTML = `<span class="status">⚠️ ${err.message}</span>`;
  } finally {
    sendBtn.disabled = false;
    inputEl.focus();
    chatEl.scrollTop = chatEl.scrollHeight;
  }
});

function escapeHtml(s) {
  return s.replace(/[&<>]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c]));
}

function showDraft(name) {
  // Drop a download card right into the conversation, under the answer.
  const wrap = document.createElement("div");
  wrap.className = "msg assistant";
  const card = document.createElement("div");
  card.className = "draft-card";
  const title = name.replace(/\.docx$/, "");
  const url = "/api/sops/download?name=" + encodeURIComponent(name);
  card.innerHTML =
    `<div class="draft-card-head">✅ <strong>Draft ready</strong> — ${escapeHtml(title)}</div>`
    + `<div class="draft-card-actions">`
    + `<a class="btn primary" href="${url}" download>⬇️ Download Word (.docx)</a>`
    + `<button type="button" class="btn" id="view-lib-btn">📄 View in SOP Library</button>`
    + `</div>`
    + `<div class="draft-card-hint">Also pinned at the top of the SOP Library, with full formatting.</div>`;
  wrap.appendChild(card);
  chatEl.appendChild(wrap);
  chatEl.scrollTop = chatEl.scrollHeight;
  card.querySelector("#view-lib-btn").addEventListener("click", () => {
    document.querySelector('.tab[data-tab="library"]').click();
  });
  if (document.querySelector('.tab[data-tab="library"]').classList.contains("active")) loadLibrary();
}

// ---------------- library ----------------
const docItemsEl = document.getElementById("doc-items");
const draftsOnlyEl = document.getElementById("drafts-only");
let allDocs = [];

async function loadLibrary() {
  try {
    const data = await (await fetch("/api/sops")).json();
    allDocs = data.documents || [];
    renderDocList();
  } catch (e) {
    docItemsEl.innerHTML = "<li class='muted'>Could not load documents.</li>";
  }
}

draftsOnlyEl.addEventListener("change", renderDocList);

function renderDocList() {
  const docs = draftsOnlyEl.checked ? allDocs.filter((d) => d.is_draft) : allDocs;
  docItemsEl.innerHTML = "";
  if (!docs.length) {
    docItemsEl.innerHTML = "<li class='muted'>No documents yet. Draft one from the Assistant tab.</li>";
    return;
  }
  docs.forEach((d) => {
    const li = document.createElement("li");
    li.innerHTML = `${d.is_draft ? "🆕 " : ""}<span class="dnum">${d.doc_number || d.title}</span> `
                 + `${d.doc_number ? escapeHtml(d.title) : ""} <span class="suffix">· ${d.suffix}</span>`;
    li.addEventListener("click", () => {
      document.querySelectorAll("#doc-items li").forEach((x) => x.classList.remove("active"));
      li.classList.add("active");
      showDoc(d);
    });
    docItemsEl.appendChild(li);
  });
}

// ---------------- manage tab ----------------
const uploadInput = document.getElementById("upload-input");
const uploadBtn = document.getElementById("upload-btn");
const uploadStatus = document.getElementById("upload-status");
const manageItems = document.getElementById("manage-doc-items");
const rebuildBtn = document.getElementById("rebuild-btn");
const rebuildStatus = document.getElementById("rebuild-status");
const manifestEl = document.getElementById("manifest");

function loadManage() {
  loadManageList();
  loadManifest();
}

async function loadManageList() {
  try {
    const data = await (await fetch("/api/sops")).json();
    const docs = (data.documents || []);
    manageItems.innerHTML = "";
    if (!docs.length) { manageItems.innerHTML = "<li class='muted'>No documents yet.</li>"; return; }
    docs.forEach((d) => {
      const li = document.createElement("li");
      const label = document.createElement("span");
      label.innerHTML = `<strong>${d.doc_number || ""}</strong> ${escapeHtml(d.title)} `
                      + `<span class="suffix">· ${d.suffix}</span>`;
      const btn = document.createElement("button");
      btn.className = "archive-btn";
      btn.textContent = "Archive";
      btn.addEventListener("click", () => archiveDoc(d.name, li));
      li.appendChild(label); li.appendChild(btn);
      manageItems.appendChild(li);
    });
  } catch (e) {
    manageItems.innerHTML = "<li class='muted'>Could not load documents.</li>";
  }
}

async function archiveDoc(name, li) {
  if (!confirm(`Archive "${name}"?\n\nIt will be moved out of the active set. Remember to Rebuild afterwards.`)) return;
  try {
    const r = await fetch("/api/sops/archive", {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name }),
    });
    if (!r.ok) throw new Error("Archive failed");
    li.remove();
    rebuildStatus.className = "status-line";
    rebuildStatus.textContent = "Archived. Click “Rebuild index now” to apply the change.";
  } catch (e) {
    alert("Could not archive: " + e.message);
  }
}

uploadBtn.addEventListener("click", async () => {
  const files = uploadInput.files;
  if (!files || !files.length) { uploadStatus.textContent = "Choose one or more files first."; return; }
  const fd = new FormData();
  for (const f of files) fd.append("files", f);
  uploadBtn.disabled = true;
  uploadStatus.className = "status-line";
  uploadStatus.textContent = "Uploading…";
  try {
    const res = await (await fetch("/api/sops/upload", { method: "POST", body: fd })).json();
    const parts = [];
    if (res.saved && res.saved.length) parts.push(`Uploaded ${res.saved.length} file(s).`);
    if (res.auto_archived && res.auto_archived.length)
      parts.push(`Auto-archived ${res.auto_archived.length} old version(s).`);
    if (res.skipped && res.skipped.length) parts.push(`Skipped ${res.skipped.length} (unsupported type).`);
    uploadStatus.className = "status-line ok";
    uploadStatus.textContent = (parts.join(" ") || "Done.") + "  Now click “Rebuild index now”.";
    uploadInput.value = "";
    loadManageList();
  } catch (e) {
    uploadStatus.className = "status-line err";
    uploadStatus.textContent = "Upload failed: " + e.message;
  } finally {
    uploadBtn.disabled = false;
  }
});

rebuildBtn.addEventListener("click", async () => {
  rebuildBtn.disabled = true;
  rebuildStatus.className = "status-line";
  rebuildStatus.textContent = "Rebuilding… this can take a moment.";
  manifestEl.innerHTML = "";
  try {
    const res = await fetch("/api/rebuild", { method: "POST" });
    if (!res.ok) {
      const detail = await res.json().catch(() => ({}));
      throw new Error(detail.detail || ("HTTP " + res.status));
    }
    const m = await res.json();
    rebuildStatus.className = "status-line ok";
    rebuildStatus.textContent = `✅ Rebuilt — ${m.document_count} document(s) indexed`
      + (m.chunks_removed ? `, ${m.chunks_removed} old entries cleared.` : ".")
      + " Open chats were reset so answers reflect the update.";
    renderManifest(m);
    loadLibrary();     // library reflects the current set too
    loadManageList();  // archived/updated docs drop out of the list
    resetChat();       // clear conversation memory so the next question re-retrieves
  } catch (e) {
    rebuildStatus.className = "status-line err";
    rebuildStatus.textContent = "Rebuild failed: " + e.message;
  } finally {
    rebuildBtn.disabled = false;
  }
});

async function loadManifest() {
  try {
    const m = await (await fetch("/api/manifest")).json();
    if (m && m.rebuilt_at) renderManifest(m);
  } catch (e) { /* none yet */ }
}

function renderManifest(m) {
  if (!m || !m.documents) { manifestEl.innerHTML = ""; return; }
  const when = m.rebuilt_at ? new Date(m.rebuilt_at).toLocaleString() : "—";
  const rows = m.documents.map((d) =>
    `<li><span class="dnum">${escapeHtml(d.doc_number || "")}</span> ${escapeHtml(d.title || "")}</li>`
  ).join("");
  manifestEl.innerHTML =
    `<div class="manifest-head">Currently indexed: ${m.document_count} document(s) · last rebuilt ${escapeHtml(when)}</div>`
    + `<ul>${rows}</ul>`;
}

async function showDoc(d) {
  document.getElementById("doc-view-empty").hidden = true;
  document.getElementById("doc-view-body").hidden = false;
  document.getElementById("doc-badge").hidden = !d.is_draft;
  document.getElementById("doc-download").href = "/api/sops/download?name=" + encodeURIComponent(d.name);

  const render = document.getElementById("doc-render");
  const md = document.getElementById("doc-md");
  if (d.suffix === "docx" && window.docx) {
    // Render the ACTUAL Word document in the browser (real tables, header, styling).
    md.hidden = true; render.hidden = false;
    render.innerHTML = "<div class='muted' style='padding:20px'>Loading…</div>";
    try {
      const blob = await (await fetch("/api/sops/download?name=" + encodeURIComponent(d.name))).blob();
      render.innerHTML = "";
      await window.docx.renderAsync(blob, render, null, {
        inWrapper: true, ignoreLastRenderedPageBreak: true,
      });
    } catch (e) {
      render.innerHTML = "<div class='muted' style='padding:20px'>Could not render this document.</div>";
    }
  } else {
    // .md / .pdf fall back to the text preview.
    render.hidden = true; md.hidden = false;
    try {
      const res = await (await fetch("/api/sops/preview?name=" + encodeURIComponent(d.name))).json();
      renderMarkdown(md, res.text || "");
    } catch (e) {
      md.textContent = "Could not load preview.";
    }
  }
}

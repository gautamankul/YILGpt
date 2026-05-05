const API_URL = "http://127.0.0.1:8000/query";

const chatBox = document.getElementById("chatBox");
const queryInput = document.getElementById("queryInput");
const sendBtn = document.getElementById("sendBtn");
const statusDot = document.getElementById("statusDot");

/* ── Helpers ─────────────────────────────────────────────── */

function getTime() {
    return new Date().toLocaleTimeString("en-US", {
        hour: "2-digit",
        minute: "2-digit",
        hour12: false,
    });
}

function setLoading(isLoading) {
    queryInput.disabled = isLoading;
    sendBtn.disabled = isLoading;
}

/* ── Message Builders ────────────────────────────────────── */

function appendUserMessage(text) {
    const row = document.createElement("div");
    row.className = "msg-row user";

    row.innerHTML = `
    <div class="msg-meta">you · ${getTime()}</div>
    <div class="bubble">${escapeHtml(text)}</div>
  `;

    chatBox.appendChild(row);
    scrollToBottom();
}

function appendBotMessage(text, source = null, isError = false) {
    const row = document.createElement("div");
    row.className = `msg-row bot${isError ? " error" : ""}`;

    const sourceHtml = source
        ? `<div class="source-tag">${escapeHtml(source)}</div>`
        : "";

    row.innerHTML = `
    <div class="msg-meta">assistant · ${getTime()}</div>
    <div class="bubble">${escapeHtml(text)}</div>
    ${sourceHtml}
  `;

    chatBox.appendChild(row);
    scrollToBottom();
}

function appendThinking() {
    const row = document.createElement("div");
    row.className = "msg-row bot";
    row.id = "thinkingRow";

    row.innerHTML = `
    <div class="msg-meta">assistant · thinking…</div>
    <div class="thinking">
      <span></span><span></span><span></span>
    </div>
  `;

    chatBox.appendChild(row);
    scrollToBottom();
    return row;
}

function removeThinking() {
    const el = document.getElementById("thinkingRow");
    if (el) el.remove();
}

function scrollToBottom() {
    chatBox.scrollTop = chatBox.scrollHeight;
}

/* ── Sanitise user-provided text ─────────────────────────── */
function escapeHtml(str) {
    return str
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;");
}

/* ── Main Query Function ─────────────────────────────────── */
async function sendQuery() {
    const question = queryInput.value.trim();
    if (!question) return;

    appendUserMessage(question);
    queryInput.value = "";
    setLoading(true);
    appendThinking();

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question }),
        });

        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }

        const data = await response.json();
        removeThinking();

        // Expects { answer: string, source?: string }
        appendBotMessage(data.answer, data.source ?? null);
        statusDot.classList.remove("offline");
        statusDot.title = "Online";

    } catch (error) {
        removeThinking();
        appendBotMessage(
            "Error: Unable to connect to the server. Make sure the API is running on port 8000.",
            null,
            true
        );
        statusDot.classList.add("offline");
        statusDot.title = "Offline";
        console.error("RAG API error:", error);
    } finally {
        setLoading(false);
        queryInput.focus();
    }
}

/* ── Keyboard Shortcut ───────────────────────────────────── */
queryInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        sendQuery();
    }
});
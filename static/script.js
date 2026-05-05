async function sendQuery() {
    const input = document.getElementById("queryInput");
    const chatBox = document.getElementById("chatBox");

    const question = input.value.trim();

    if (!question) return;

    // Show user message
    chatBox.innerHTML += `<div class="message user">${question}</div>`;

    input.value = "";

    try {
        const response = await fetch("http://127.0.0.1:8000/query", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question })
        });

        const data = await response.json();

        chatBox.innerHTML += `<div class="message bot">${data.answer}</div>`;

        chatBox.scrollTop = chatBox.scrollHeight;

    } catch (error) {
        chatBox.innerHTML += `<div class="message bot">Error: Unable to connect</div>`;
    }
}
async function sendMessage() {

    const input = document.getElementById("message");
    const chatBox = document.getElementById("messages");

    const message = input.value.trim();

    if (message === "") {
        return;
    }

    // Privacy consent check
    const privacyCheck = document.getElementById("privacyCheck");

    if (!privacyCheck.checked) {
        alert("Please read and acknowledge the Privacy & Safety notice before using Lotus AI.");
        return;
    }

    // Show user's message safely
    chatBox.innerHTML += `
        <p>
            <b>You:</b> ${escapeHTML(message)}
        </p>
    `;

    input.value = "";

    try {

        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        // Show Lotus AI response
        chatBox.innerHTML += `
            <p>
                <b>Lotus AI:</b>
            </p>

            <div class="ai-response">
                ${formatAIResponse(data.reply)}
            </div>
        `;

        chatBox.scrollTop = chatBox.scrollHeight;

    } catch (error) {

        chatBox.innerHTML += `
            <p>
                <b>Lotus AI:</b>
            </p>

            <div class="ai-response">
                Sorry, I couldn't connect to the server.
            </div>
        `;
    }
}


/* Prevent user-entered HTML from being interpreted by the browser */
function escapeHTML(text) {

    const div = document.createElement("div");

    div.textContent = text;

    return div.innerHTML;
}


/* Format Gemini's response */
function formatAIResponse(text) {

    // Escape HTML first
    text = escapeHTML(text);

    // Bold Markdown: **text**
    text = text.replace(
        /\*\*(.*?)\*\*/g,
        "<strong>$1</strong>"
    );

    // Markdown headings
    text = text.replace(
        /^###\s+(.*)$/gm,
        "<h4>$1</h4>"
    );

    text = text.replace(
        /^##\s+(.*)$/gm,
        "<h3>$1</h3>"
    );

    text = text.replace(
        /^#\s+(.*)$/gm,
        "<h2>$1</h2>"
    );

    // Numbered lists
    text = text.replace(
        /^\s*(\d+)\.\s+(.*)$/gm,
        "<div class=\"numbered-item\"><strong>$1.</strong> $2</div>"
    );

    // Bullet points
    text = text.replace(
        /^\s*[-*•]\s+(.*)$/gm,
        "<div class=\"bullet-item\">• $1</div>"
    );

    // Preserve paragraph spacing
    text = text.replace(
        /\n{2,}/g,
        "<br><br>"
    );

    // Preserve normal line breaks
    text = text.replace(
        /\n/g,
        "<br>"
    );

    return text;
}

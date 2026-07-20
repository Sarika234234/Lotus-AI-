async function sendMessage() {

    const input = document.getElementById("message");
    const chatBox = document.getElementById("messages");

    const message = input.value.trim();

    if (message === "") {
        return;
    }

    chatBox.innerHTML += `<p><b>You:</b> ${message}</p>`;

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

        chatBox.innerHTML += `<p><b>Lotus AI:</b> ${data.reply}</p>`;
        chatBox.scrollTop = chatBox.scrollHeight;

    } catch (error) {
        chatBox.innerHTML += `<p><b>Lotus AI:</b> Error connecting to the server.</p>`;
    }
}

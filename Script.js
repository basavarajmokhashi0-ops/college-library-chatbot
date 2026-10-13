const chatForm = document.getElementById("chatForm");
const messageInput = document.getElementById("messageInput");
const chatBox = document.getElementById("chatBox");


// Display a message in the chatbot
function addMessage(message, className) {
    const div = document.createElement("div");

    div.className = className;
    div.textContent = message;

    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}


// Send a message to Python
chatForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const message = messageInput.value.trim();

    if (!message) {
        return;
    }

    addMessage(message, "user-message");
    messageInput.value = "";

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

        addMessage(data.reply, "bot-message");

    } catch (error) {
        addMessage(
            "Unable to connect to the chatbot. Please try again.",
            "bot-message"
        );
    }
});


// Search books instantly on the page
const searchInput = document.getElementById("searchInput");

searchInput.addEventListener("input", function () {
    const search = searchInput.value.toLowerCase();

    const cards = document.querySelectorAll(".book-card");

    cards.forEach(function (card) {
        const text = card.textContent.toLowerCase();

        card.style.display = text.includes(search)
            ? ""
            : "none";
    });
});
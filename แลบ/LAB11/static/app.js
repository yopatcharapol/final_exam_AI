let currentChatId = null;


async function loadChats() {
    const response = await fetch("/api/chats");

    const chats = await response.json();

    const chatList = document.getElementById("chat-list");

    chatList.innerHTML = "";

    chats.forEach(chat => {
        const chatItem = document.createElement("div");

        chatItem.className = "chat-item";

        if (chat.id === currentChatId) {
            chatItem.classList.add("active");
        }

        chatItem.textContent = chat.title;

        chatItem.onclick = () => {
            openChat(chat.id);
        };

        chatList.appendChild(chatItem);
    });
}


async function createNewChat() {
    const response = await fetch(
        "/api/chats",
        {
            method: "POST"
        }
    );

    const chat = await response.json();

    currentChatId = chat.id;

    await loadChats();

    document.getElementById("messages").innerHTML = `
        <div class="empty-message">
            Start a new conversation.
        </div>
    `;

    document
        .getElementById("message-input")
        .focus();
}


async function openChat(chatId) {
    currentChatId = chatId;

    const response = await fetch(
        `/api/chats/${chatId}`
    );

    const data = await response.json();

    const messagesContainer =
        document.getElementById("messages");

    messagesContainer.innerHTML = "";

    data.messages.forEach(message => {
        addMessageToScreen(
            message.role,
            message.content
        );
    });

    scrollToBottom();

    await loadChats();
}


function addMessageToScreen(role, content) {
    const messagesContainer =
        document.getElementById("messages");

    const messageElement =
        document.createElement("div");

    messageElement.className =
        `message ${role}`;

    messageElement.textContent = content;

    messagesContainer.appendChild(
        messageElement
    );
}


async function sendMessage() {
    const input =
        document.getElementById(
            "message-input"
        );

    const content = input.value.trim();

    if (!content) {
        return;
    }


    // Automatically create chat if none exists
    if (!currentChatId) {
        await createNewChat();
    }


    // Show user message immediately
    addMessageToScreen(
        "user",
        content
    );

    input.value = "";

    scrollToBottom();


    // Disable input while waiting
    input.disabled = true;

    const sendButton =
        document.getElementById(
            "send-button"
        );

    sendButton.disabled = true;


    // Add temporary loading message
    const messagesContainer =
        document.getElementById("messages");

    const loadingElement =
        document.createElement("div");

    loadingElement.className =
        "message assistant loading";

    loadingElement.textContent =
        "Thinking...";

    messagesContainer.appendChild(
        loadingElement
    );

    scrollToBottom();


    try {

        const response = await fetch(
            `/api/chats/${currentChatId}/messages`,
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    content: content
                })
            }
        );


        const data = await response.json();


        // Remove loading message
        loadingElement.remove();


        if (!response.ok) {
            throw new Error(
                data.detail ||
                "Something went wrong"
            );
        }


        // Display assistant answer
        addMessageToScreen(
            "assistant",
            data.content
        );

        await loadChats();

    }
    catch (error) {

        loadingElement.remove();

        addMessageToScreen(
            "assistant",
            "Error: " + error.message
        );
    }
    finally {

        input.disabled = false;

        sendButton.disabled = false;

        input.focus();

        scrollToBottom();
    }
}


function scrollToBottom() {
    const messagesContainer =
        document.getElementById("messages");

    messagesContainer.scrollTop =
        messagesContainer.scrollHeight;
}


// Send message using Enter
document
    .getElementById("message-input")
    .addEventListener(
        "keydown",
        function(event) {

            if (
                event.key === "Enter" &&
                !event.shiftKey
            ) {
                event.preventDefault();

                sendMessage();
            }
        }
    );


// Load history when website opens
loadChats();


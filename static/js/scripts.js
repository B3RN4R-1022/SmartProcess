document.addEventListener("DOMContentLoaded", function () {
    const apiKeyIcon = document.getElementById("api-key-icon");
    const apiKeyInput = document.getElementById("api-key-input");

    apiKeyIcon.addEventListener("click", function () {
        const apiKey = prompt("Digite sua chave API:");
        if (apiKey !== null) {
            apiKeyInput.value = apiKey;
        }
    });

    const promptSelect = document.getElementById("prompt-selector");
    const userInput = document.getElementById("user-input");
    const submitButton = document.getElementById("arrow-icon");
    const conversationContainer = document.querySelector(".conversation-container");

    submitButton.addEventListener("click", async function () {
        const selectedPrompt = promptSelect.value;
        const userMessage = userInput.value;

        if (userMessage.trim() !== "") {
            appendMessage("user-message", userMessage);

            const response = await fetch("/submit", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                body: `prompt=${selectedPrompt}&user_input=${userMessage}`
            });

            const responseData = await response.json();
            const assistantResponse = responseData.response;

            appendMessage("assistant-message", assistantResponse);

            userInput.value = "";
            conversationContainer.scrollTop = conversationContainer.scrollHeight;
        }
    });


    function appendMessage(className, message) {
        const messageElement = document.createElement("div");
        messageElement.classList.add("message", className);
        messageElement.textContent = message;
        conversationContainer.appendChild(messageElement);
    }

    userInput.addEventListener("keydown", function(event) {
        // Verifica se a tecla pressionada foi Enter e se não está pressionando a tecla Shift junto
        if (event.key === "Enter" && !event.shiftKey) {
            event.preventDefault(); // Evita a ação padrão do Enter (por exemplo, quebra de linha)
            submitButton.click();
        }
    });
});

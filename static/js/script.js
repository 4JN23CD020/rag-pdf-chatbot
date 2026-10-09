// ======================================================
// RAG PDF CHATBOT - CLEAN FRONTEND
// ======================================================

const API = "";

const pdfInput = document.getElementById("pdfInput");
const uploadBtn = document.getElementById("uploadBtn");
const sendBtn = document.getElementById("sendBtn");
const questionBox = document.getElementById("question");
const chatBox = document.getElementById("chatBox");
const documentList = document.getElementById("documentList");
const typing = document.getElementById("typing");

// ======================================================
// NOTIFICATION
// ======================================================

function showNotification(message) {
    alert(message);
}

// ======================================================
// LOAD DOCUMENTS
// ======================================================

async function loadDocuments() {

    try {

        const response = await fetch("/upload/list");

        if (!response.ok) {
            throw new Error("Could not load documents");
        }

        const data = await response.json();

        documentList.innerHTML = "";

        data.documents.forEach(function (filename) {

            const li = document.createElement("li");

            li.innerHTML = `
                📄 ${filename}
                <button type="button"
                        onclick="deleteDocument(${JSON.stringify(filename)})">
                    ❌
                </button>
            `;

            documentList.appendChild(li);

        });

        console.log("Documents:", data.documents);

    } catch (error) {

        console.error("Load documents error:", error);

    }
}

// ======================================================
// UPLOAD PDF
// ======================================================

async function uploadPDF() {

    console.log("Upload button clicked");

    if (!pdfInput.files || pdfInput.files.length === 0) {

        showNotification("Please select a PDF first.");

        return;
    }

    const formData = new FormData();

    for (const file of pdfInput.files) {

        console.log("Selected file:", file.name);

        formData.append("files", file);

    }

    try {

        uploadBtn.disabled = true;
        uploadBtn.innerText = "Uploading...";

        console.log("Sending POST /upload/");

        const response = await fetch("/upload/", {
            method: "POST",
            body: formData
        });

        console.log("Upload response:", response.status);

        const data = await response.json();

        console.log("Upload result:", data);

        if (!response.ok) {

            throw new Error(
                data.message || data.detail || "Upload failed"
            );
        }

        showNotification(
            "Upload successful: " +
            data.uploaded_files.join(", ")
        );

        pdfInput.value = "";

        await loadDocuments();

    } catch (error) {

        console.error("UPLOAD ERROR:", error);

        showNotification(
            "Upload failed: " + error.message
        );

    } finally {

        uploadBtn.disabled = false;
        uploadBtn.innerText = "Upload";

    }
}

// ======================================================
// DELETE DOCUMENT
// ======================================================

async function deleteDocument(filename) {

    const confirmed = confirm(
        "Delete " + filename + "?"
    );

    if (!confirmed) {
        return;
    }

    try {

        const response = await fetch(
            "/upload/" + encodeURIComponent(filename),
            {
                method: "DELETE"
            }
        );

        const data = await response.json();

        console.log("Delete result:", data);

        await loadDocuments();

    } catch (error) {

        console.error("Delete error:", error);

        showNotification("Delete failed.");

    }
}

// ======================================================
// ASK QUESTION
// ======================================================

async function askQuestion() {

    console.log("Send button clicked");

    const question = questionBox.value.trim();

    if (!question) {

        showNotification("Please enter a question.");

        return;
    }

    addUserMessage(question);

    questionBox.value = "";

    if (typing) {
        typing.style.display = "block";
    }

    sendBtn.disabled = true;
    sendBtn.innerText = "Thinking...";

    try {

        console.log("Sending POST /query/");

        const response = await fetch("/query/", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })

        });

        console.log(
            "Query response:",
            response.status
        );

        const data = await response.json();

        console.log("Query result:", data);

        if (!response.ok) {

            throw new Error(
                data.detail || "Question failed"
            );
        }

        addAIMessage(data.answer);

    } catch (error) {

        console.error("QUERY ERROR:", error);

        addAIMessage(
            "Sorry, I could not get an answer. " +
            error.message
        );

    } finally {

        if (typing) {
            typing.style.display = "none";
        }

        sendBtn.disabled = false;
        sendBtn.innerText = "Send";

    }
}

// ======================================================
// ADD USER MESSAGE
// ======================================================

function addUserMessage(message) {

    const div = document.createElement("div");

    div.className = "message user";

    div.innerHTML = `
        <div class="avatar">👤</div>

        <div class="bubble">
            <p>${escapeHTML(message)}</p>
        </div>
    `;

    chatBox.appendChild(div);

    scrollChat();
}

// ======================================================
// ADD AI MESSAGE
// ======================================================

function addAIMessage(message) {

    const div = document.createElement("div");

    div.className = "message ai";

    div.innerHTML = `
        <div class="avatar">🤖</div>

        <div class="bubble">

            <h3>Assistant</h3>

            <p>${escapeHTML(message)}</p>

        </div>
    `;

    chatBox.appendChild(div);

    scrollChat();
}

// ======================================================
// ESCAPE HTML
// ======================================================

function escapeHTML(text) {

    const div = document.createElement("div");

    div.textContent = text;

    return div.innerHTML;
}

// ======================================================
// SCROLL CHAT
// ======================================================

function scrollChat() {

    chatBox.scrollTop = chatBox.scrollHeight;

}

// ======================================================
// BUTTON EVENTS
// ======================================================

if (uploadBtn) {

    uploadBtn.addEventListener(
        "click",
        uploadPDF
    );

}

if (sendBtn) {

    sendBtn.addEventListener(
        "click",
        askQuestion
    );

}

// ======================================================
// ENTER KEY
// ======================================================

if (questionBox) {

    questionBox.addEventListener(
        "keydown",
        function (event) {

            if (
                event.key === "Enter" &&
                !event.shiftKey
            ) {

                event.preventDefault();

                askQuestion();

            }

        }
    );

}

// ======================================================
// PAGE LOAD
// ======================================================

document.addEventListener(
    "DOMContentLoaded",
    function () {

        console.log(
            "RAG PDF Chatbot JavaScript loaded."
        );

        loadDocuments();

    }
);
# 🤖 RAG PDF Chatbot

An AI-powered PDF chatbot that allows users to upload PDF documents and ask questions about their content. It uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from documents and generate context-aware answers.

## 📌 Project Overview

Reading and searching lengthy PDF documents manually can be time-consuming. This project simplifies the process by allowing users to upload PDFs and interact with their content through a conversational interface.

The application extracts text from PDF documents, splits the text into smaller chunks, converts those chunks into embeddings, and retrieves relevant content to answer user questions.

## ✨ Features

* 📄 Upload and process PDF documents.
* 🧹 Extract and clean text from PDFs.
* ✂️ Split text into manageable chunks.
* 🔎 Retrieve relevant document content for user questions.
* 🧠 Generate context-aware answers using an AI language model.
* 💬 Interact with PDF content through a chatbot interface.
* 🌐 Web interface built with HTML, CSS, and JavaScript.
* 🔐 Environment-variable-based API key configuration.

## 🏗️ Architecture

The application follows a Retrieval-Augmented Generation workflow:

1. **PDF Upload:** The user uploads a PDF document.
2. **Text Extraction:** Text is extracted from the PDF.
3. **Text Cleaning:** Unnecessary whitespace and unwanted characters are cleaned.
4. **Text Chunking:** Extracted text is divided into smaller chunks.
5. **Embedding Generation:** Text chunks are converted into vector embeddings.
6. **Vector Storage:** Embeddings are stored for similarity-based retrieval.
7. **Question Processing:** The user submits a question.
8. **Retrieval:** Relevant chunks are retrieved from the document.
9. **Answer Generation:** The retrieved context is passed to an AI model to generate an answer.
10. **Response Display:** The answer is displayed in the chatbot interface.

## 🛠️ Technologies Used

| Technology                   | Purpose                                          |
| ---------------------------- | ------------------------------------------------ |
| Python                       | Backend development                              |
| FastAPI                      | Web API and application endpoints                |
| HTML                         | Frontend structure                               |
| CSS                          | Frontend styling                                 |
| JavaScript                   | Chatbot interactions                             |
| PyMuPDF                      | PDF text extraction                              |
| Embedding models             | Convert text into vector representations         |
| Vector store                 | Store and retrieve document embeddings           |
| Google Gemini API / Grok API | AI model integration, depending on configuration |
| Git and GitHub               | Version control and source code hosting          |

*The exact models, vector-store implementation, and API provider depend on your project's current configuration.*

## 📂 Project Structure

```text
rag-pdf-chatbot/
│
├── app.py
├── list_module.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── backend/
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   │
│   ├── rag/
│   │   ├── __init__.py
│   │   ├── chunker.py
│   │   ├── embeddings.py
│   │   ├── grok_client.py
│   │   ├── ingest.py
│   │   ├── pdf_loader.py
│   │   ├── prompt_builder.py
│   │   ├── rag_pipeline.py
│   │   ├── retriever.py
│   │   ├── text_cleaner.py
│   │   └── vector_store.py
│   │
│   └── routes/
│       ├── __init__.py
│       ├── database.py
│       ├── query.py
│       └── upload.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
└── templates/
    └── index.html
```

*Generated databases, uploaded PDFs, virtual environments, and environment files are excluded from this overview.*

## ⚙️ Installation and Setup

### Prerequisites

Make sure you have installed:

* Python 3.10 or a compatible version required by your dependencies.
* Git.
* A supported AI provider API key.
* Visual Studio Code or another Python-compatible editor (optional).

### 1. Clone the repository

```bash
git clone https://github.com/4JN23CD020/rag-pdf-chatbot.git
```

### 2. Navigate to the project directory

```bash
cd rag-pdf-chatbot
```

### 3. Create a virtual environment

On Windows:

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Command Prompt:

```bash
.venv\Scripts\activate
```

PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file in the project's root directory.

Add the environment variables required by your application. For example:

```env
GOOGLE_API_KEY=your_new_google_api_key
GROK_API_KEY=your_grok_api_key
```

Replace the placeholders with valid keys from the providers you actually use. Do not commit your `.env` file to GitHub.

**Security note:** If an API key has previously been exposed, revoke or rotate it before using a replacement.

The application must load `.env` variables explicitly, for example with `python-dotenv`, unless they are already supplied by your environment or deployment platform.

Only configure the provider variables required by your application's code.

## ▶️ Running the Application

The correct startup command depends on how your application is configured.

If `app.py` defines a FastAPI application named `app`, try:

```bash
uvicorn app:app --reload
```

If the FastAPI application is defined in `backend/main.py`, the command may instead be:

```bash
uvicorn backend.main:app --reload
```

Use the command that matches the actual application object in your project.

After the server starts, open the local address printed in the terminal. For a typical local FastAPI server, this is:

```text
http://127.0.0.1:8000
```

FastAPI applications commonly expose interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

These addresses apply only if your application uses the default host and port.

## 🔐 Security Best Practices

* Never hardcode API keys in Python files.
* Store API keys in environment variables or a secret manager.
* Keep `.env` excluded from Git.
* Never upload private PDFs or sensitive documents without authorization.
* Avoid committing virtual environments and generated files.
* Rotate API keys immediately if they are exposed.
* Review changes before pushing them to GitHub.
* Restrict API keys to the required services and permissions where possible.

## 🚧 Current Limitations

Potential limitations depend on the implementation:

* Answer quality depends on PDF text extraction and retrieval accuracy.
* Scanned PDFs may require optical character recognition (OCR).
* Large documents may require additional processing time and memory.
* AI responses may occasionally be inaccurate or omit relevant details.
* API usage may be subject to provider quotas and costs.

## 🔮 Future Enhancements

* Support multiple PDF documents.
* Add conversation history.
* Display source references for generated answers.
* Support scanned PDFs through OCR.
* Improve semantic search and retrieval quality.
* Add authentication and user-specific document storage.
* Deploy the application to a cloud platform.
* Add automated tests and continuous integration.

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test your changes.
5. Submit a pull request.

## 📄 License

No license has been specified yet. Unless a license is added, others generally do not receive an explicit open-source license to reuse, modify, or distribute this project's code.

## 👨‍💻 Author

**GitHub:** [4JN23CD020](https://github.com/4JN23CD020)

---

⭐ If you find this project useful, consider starring the repository!

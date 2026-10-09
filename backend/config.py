"""
====================================================
RAG PDF CHATBOT CONFIGURATION
====================================================
Author : AnanthaKrishna M Ghate
Description :
Central configuration file for the entire project.
No .env file required.
====================================================
"""

import os
from pathlib import Path

# ====================================================
# PROJECT
# ====================================================

PROJECT_NAME = "RAG PDF Chatbot"

VERSION = "1.0.0"

# Change only this path if you move the project
PROJECT_ROOT = Path(r"D:\rag-pdf-chatbot")

# ====================================================
# SERVER
# ====================================================

HOST = "127.0.0.1"

PORT = 8000

DEBUG = True

# ====================================================
# DIRECTORIES
# ====================================================

BACKEND_DIR = PROJECT_ROOT / "backend"

UPLOAD_DIR = PROJECT_ROOT / "uploads"

DATABASE_DIR = PROJECT_ROOT / "database"

VECTOR_DB_DIR = DATABASE_DIR / "faiss"

CACHE_DIR = PROJECT_ROOT / "cache"

LOG_DIR = PROJECT_ROOT / "logs"

STATIC_DIR = PROJECT_ROOT / "static"

TEMPLATE_DIR = PROJECT_ROOT / "templates"

# ====================================================
# VECTOR DATABASE FILES
# ====================================================

FAISS_INDEX = VECTOR_DB_DIR / "index.faiss"

FAISS_METADATA = VECTOR_DB_DIR / "metadata.pkl"

DOCUMENT_DATABASE = VECTOR_DB_DIR / "documents.json"

# ====================================================
# EMBEDDING MODEL
# ====================================================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ====================================================
# TEXT CHUNKING
# ====================================================

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200

TOP_K_RESULTS = 5

# ====================================================
# GROK API
# ====================================================

#GROK_API_KEY = ""

#GROK_MODEL = "grok-4"

# Replace with the correct endpoint if your Grok account uses a different URL.
#GROK_API_URL = "https://api.x.ai/v1/chat/completions"

#TEMPERATURE = 0.2

#MAX_TOKENS = 2048

# ====================================================
# ALLOWED FILES
# ====================================================

ALLOWED_EXTENSIONS = [
    ".pdf"
]

MAX_FILE_SIZE_MB = 100

# ====================================================
# CHAT SETTINGS
# ====================================================

MAX_CHAT_HISTORY = 10

SYSTEM_PROMPT = """
You are a PDF Question Answering Assistant.

Rules:

1. Answer ONLY using the retrieved document context.

2. Never make up information.

3. If the answer is unavailable, reply:

'I couldn't find that information in the uploaded documents.'

4. Be concise.

5. Mention page numbers whenever possible.
"""

# ====================================================
# CREATE REQUIRED DIRECTORIES
# ====================================================

REQUIRED_DIRS = [
    UPLOAD_DIR,
    DATABASE_DIR,
    VECTOR_DB_DIR,
    CACHE_DIR,
    LOG_DIR,
    STATIC_DIR,
    TEMPLATE_DIR,
]

for directory in REQUIRED_DIRS:
    directory.mkdir(parents=True, exist_ok=True)

# Compatibility aliases
UPLOAD_FOLDER = UPLOAD_DIR
FAISS_FOLDER = VECTOR_DB_DIR

if __name__ == "__main__":
    print("Configuration Loaded Successfully.")
# ====================================================
# GEMINI
# ====================================================

api_key = os.getenv("GOOGLE_API_KEY")

GEMINI_MODEL = "gemini-3.5-flash"
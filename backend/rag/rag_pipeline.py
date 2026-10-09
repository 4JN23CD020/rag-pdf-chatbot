"""
=========================================================
RAG PIPELINE
=========================================================
"""

from backend.rag.pdf_loader import load_pdf
from backend.rag.text_cleaner import clean_documents
from backend.rag.chunker import create_chunks

from backend.rag.embeddings import embed_chunks
from backend.rag.vector_store import add_embeddings

from backend.rag.retriever import get_context
from backend.rag.prompt_builder import create_prompt
from backend.rag.grok_client import ask_grok


# --------------------------------------------------------
# Process Uploaded PDF
# --------------------------------------------------------

def process_pdf(pdf_path):

    pages = load_pdf(pdf_path)

    pages = clean_documents(pages)

    chunks = create_chunks(pages)

    embedded_chunks = embed_chunks(chunks)

    add_embeddings(embedded_chunks)

    print(f"Indexed: {pdf_path}")


# --------------------------------------------------------
# Generate Answer
# --------------------------------------------------------

def generate_answer(question):

    context, sources = get_context(question)

    # Pass the retrieved documents, not the context string
    prompt = create_prompt(question, sources)

    answer = ask_grok(prompt)

    return {
        "answer": answer,
        "sources": sources
    }


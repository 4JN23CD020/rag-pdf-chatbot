"""
=========================================================
PDF INGESTION PIPELINE
=========================================================
Loads PDFs → Chunks → Embeddings → FAISS
=========================================================
"""

from backend.config import UPLOAD_DIR
from backend.rag.pdf_loader import load_all_pdfs
from backend.rag.chunker import create_chunks
from backend.rag.embeddings import create_embeddings
from backend.rag.vector_store import save_to_vector_store, database_stats


def ingest():

    print("=" * 60)
    print("Loading PDFs...")
    print("=" * 60)

    documents = load_all_pdfs(UPLOAD_DIR)

    print(f"Pages Loaded : {len(documents)}")

    if not documents:
        print("No PDF documents found.")
        return

    print("\nCreating Chunks...")
    chunks = create_chunks(documents)

    print(f"Chunks Created : {len(chunks)}")

    print("\nGenerating Embeddings...")
    embedded_chunks = create_embeddings(chunks)

    print(f"Embeddings Generated : {len(embedded_chunks)}")

    print("\nSaving to FAISS...")
    save_to_vector_store(chunks, embedded_chunks)

    print("\nDatabase Statistics")
    print(database_stats())

    print("\nIngestion Completed Successfully.")


if __name__ == "__main__":
    ingest()
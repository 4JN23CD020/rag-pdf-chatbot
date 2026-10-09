"""
=========================================================
EMBEDDING GENERATOR
=========================================================
Converts text chunks into vector embeddings.
=========================================================
"""

import numpy as np

from sentence_transformers import SentenceTransformer

from backend.config import EMBEDDING_MODEL

# =========================================================
# Load Model Only Once
# =========================================================

print(f"Loading embedding model: {EMBEDDING_MODEL}")

model = SentenceTransformer(EMBEDDING_MODEL)

print("Embedding model loaded.")

model = SentenceTransformer(EMBEDDING_MODEL)

print("Embedding Model Loaded Successfully.\n")


class EmbeddingGenerator:

    def __init__(self):

        self.model = model

    # -----------------------------------------------------
    # Single Text Embedding
    # -----------------------------------------------------

    def encode_text(self, text):

        embedding = self.model.encode(

            text,

            normalize_embeddings=True,

            convert_to_numpy=True

        )

        return embedding.astype("float32")

    # -----------------------------------------------------
    # Batch Embedding
    # -----------------------------------------------------

    def encode_texts(self, texts):

        embeddings = self.model.encode(

            texts,

            batch_size=32,

            show_progress_bar=True,

            normalize_embeddings=True,

            convert_to_numpy=True

        )

        return embeddings.astype("float32")

    # -----------------------------------------------------
    # Chunk Embedding
    # -----------------------------------------------------

    def encode_chunks(self, chunks):

        texts = []

        for chunk in chunks:

            texts.append(chunk["text"])

        vectors = self.encode_texts(texts)

        embedded_chunks = []

        for chunk, vector in zip(chunks, vectors):

            embedded_chunks.append({

                "chunk_id": chunk["chunk_id"],

                "document": chunk["document"],

                "page": chunk["page"],

                "chunk_number": chunk["chunk_number"],

                "text": chunk["text"],

                "embedding": vector

            })

        return embedded_chunks


# =========================================================
# Helper Functions
# =========================================================

generator = EmbeddingGenerator()


def embed_query(question):

    return generator.encode_text(question)


def embed_chunks(chunks):

    return generator.encode_chunks(chunks)


# =========================================================
# Testing
# =========================================================

if __name__ == "__main__":

    sample = [

        {

            "chunk_id": "1",

            "document": "Python.pdf",

            "page": 1,

            "chunk_number": 1,

            "text": "Python is a programming language."

        },

        {

            "chunk_id": "2",

            "document": "Python.pdf",

            "page": 2,

            "chunk_number": 2,

            "text": "Machine Learning uses Python."

        }

    ]

    result = embed_chunks(sample)

    print()

    print("Chunks :", len(result))

    print()

    print("Embedding Shape :")

    print(result[0]["embedding"].shape)

# =========================================================
# Compatibility Function
# =========================================================

def create_embeddings(chunks):
    """
    Compatibility wrapper for rag_pipeline.py
    """
    return embed_chunks(chunks)
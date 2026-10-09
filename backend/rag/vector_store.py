"""
=========================================================
FAISS VECTOR DATABASE
=========================================================
Stores embeddings and retrieves similar chunks.
=========================================================
"""

import pickle
import faiss
import numpy as np

from backend.config import (
    FAISS_INDEX,
    FAISS_METADATA,
    TOP_K_RESULTS
)


class VectorStore:

    def __init__(self):

        # all-MiniLM-L6-v2 embedding dimension
        self.dimension = 384

        self.index = None

        self.metadata = []

        self.load_database()

    # ----------------------------------------------------
    # Create Empty Index
    # ----------------------------------------------------

    def create_index(self):

        self.index = faiss.IndexFlatIP(self.dimension)

        self.metadata = []

    # ----------------------------------------------------
    # Load Existing Database
    # ----------------------------------------------------

    def load_database(self):

        if FAISS_INDEX.exists() and FAISS_METADATA.exists():

            self.index = faiss.read_index(str(FAISS_INDEX))

            with open(FAISS_METADATA, "rb") as file:

                self.metadata = pickle.load(file)

            print("Existing FAISS Database Loaded.")

        else:

            self.create_index()

            print("New FAISS Database Created.")

    # ----------------------------------------------------
    # Save Database
    # ----------------------------------------------------

    def save_database(self):

        faiss.write_index(

            self.index,

            str(FAISS_INDEX)

        )

        with open(

            FAISS_METADATA,

            "wb"

        ) as file:

            pickle.dump(

                self.metadata,

                file

            )

        print("Database Saved.")

    # ----------------------------------------------------
    # Add Embeddings
    # ----------------------------------------------------

    def add_chunks(self, embedded_chunks):

        if len(embedded_chunks) == 0:

            return

        vectors = []

        documents = []

        for chunk in embedded_chunks:

            vectors.append(chunk["embedding"])

            documents.append({

                "chunk_id": chunk["chunk_id"],

                "document": chunk["document"],

                "page": chunk["page"],

                "chunk_number": chunk["chunk_number"],

                "text": chunk["text"]

            })

        vectors = np.array(

            vectors,

            dtype=np.float32

        )

        self.index.add(vectors)

        self.metadata.extend(documents)

        self.save_database()

    # ----------------------------------------------------
    # Similarity Search
    # ----------------------------------------------------

    def search(

        self,

        query_vector,

        top_k=TOP_K_RESULTS

    ):

        if self.index.ntotal == 0:

            return []

        query = np.array(

            [query_vector],

            dtype=np.float32

        )

        scores, indices = self.index.search(

            query,

            top_k

        )

        results = []

        for score, idx in zip(

            scores[0],

            indices[0]

        ):

            if idx == -1:

                continue

            item = self.metadata[idx].copy()

            item["score"] = float(score)

            results.append(item)

        return results

    # ----------------------------------------------------
    # Statistics
    # ----------------------------------------------------

    def stats(self):

        return {

            "vectors": self.index.ntotal,

            "documents": len(self.metadata)

        }

    # ----------------------------------------------------
    # Reset Database
    # ----------------------------------------------------

    def reset(self):

        self.create_index()

        self.save_database()

        print("Database Reset Successfully.")


# ======================================================
# Singleton Object
# ======================================================

vector_db = VectorStore()


# ======================================================
# Helper Functions
# ======================================================

def add_embeddings(embedded_chunks):

    vector_db.add_chunks(embedded_chunks)


def save_to_vector_store(chunks, embedded_chunks):
    """
    Compatibility function for rag_pipeline.py

    'chunks' is ignored because embedded_chunks already
    contains all metadata and embeddings.
    """

    add_embeddings(embedded_chunks)


def similarity_search(

    query_vector,

    top_k=TOP_K_RESULTS

):

    return vector_db.search(

        query_vector,

        top_k

    )


def database_stats():

    return vector_db.stats()


def reset_database():

    vector_db.reset()


# ======================================================
# Testing
# ======================================================

if __name__ == "__main__":

    print(database_stats())
# ======================================================
# Compatibility Function
# ======================================================

def save_to_vector_store(chunks, embedded_chunks):
    """
    Compatibility wrapper for rag_pipeline.py

    Parameters:
        chunks: ignored (already included in embedded_chunks)
        embedded_chunks: output of create_embeddings()
    """
    add_embeddings(embedded_chunks)
def reset_database():
    vector_db.reset()


# ======================================================
# Compatibility Function
# ======================================================

def save_to_vector_store(chunks, embedded_chunks):
    add_embeddings(embedded_chunks)
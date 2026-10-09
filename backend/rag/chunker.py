"""
=========================================================
TEXT CHUNKER
=========================================================
Splits cleaned PDF text into overlapping chunks.
=========================================================
"""

import uuid

from langchain_text_splitters import RecursiveCharacterTextSplitter

from backend.config import CHUNK_SIZE, CHUNK_OVERLAP


class DocumentChunker:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(

            chunk_size=CHUNK_SIZE,

            chunk_overlap=CHUNK_OVERLAP,

            separators=[
                "\n\n",
                "\n",
                ". ",
                "? ",
                "! ",
                "; ",
                ", ",
                " ",
                ""
            ]
        )

    # ---------------------------------------------------
    # Chunk One Document
    # ---------------------------------------------------

    def chunk_document(self, document):

        chunks = self.splitter.split_text(document["text"])

        result = []

        for index, chunk in enumerate(chunks):

            result.append({

                "chunk_id": str(uuid.uuid4()),

                "document": document["document"],

                "page": document["page"],

                "chunk_number": index + 1,

                "text": chunk

            })

        return result

    # ---------------------------------------------------
    # Chunk Multiple Documents
    # ---------------------------------------------------

    def chunk_documents(self, documents):

        all_chunks = []

        for document in documents:

            chunks = self.chunk_document(document)

            all_chunks.extend(chunks)

        return all_chunks


# =========================================================
# Helper Function
# =========================================================

def create_chunks(documents):

    chunker = DocumentChunker()

    return chunker.chunk_documents(documents)


# =========================================================
# Testing
# =========================================================

if __name__ == "__main__":

    sample = [

        {

            "document": "Python.pdf",

            "page": 1,

            "text": "Python is a programming language. " * 300

        }

    ]

    chunks = create_chunks(sample)

    print()

    print("Total Chunks :", len(chunks))

    print()

    for chunk in chunks[:3]:

        print("=" * 60)

        print("Chunk ID :", chunk["chunk_id"])

        print("Document :", chunk["document"])

        print("Page :", chunk["page"])

        print("Chunk :", chunk["chunk_number"])

        print()

        print(chunk["text"][:300])
# =========================================================
# Compatibility Function
# =========================================================

def split_into_chunks(documents):

    return create_chunks(documents)
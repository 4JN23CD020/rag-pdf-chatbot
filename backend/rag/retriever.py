"""
=========================================================
RETRIEVER
=========================================================
Retrieves the most relevant chunks from FAISS.
=========================================================
"""

from backend.config import TOP_K_RESULTS
from backend.rag.embeddings import embed_query
from backend.rag.vector_store import similarity_search


class Retriever:

    def __init__(self):
        pass

    # ----------------------------------------------------
    # Search Similar Chunks
    # ----------------------------------------------------

    def retrieve(self, question, top_k=TOP_K_RESULTS):

        question = question.strip()

        if not question:
            return []

        query_embedding = embed_query(question)

        results = similarity_search(
            query_embedding,
            top_k
        )

        return results

    # ----------------------------------------------------
    # Build Context String
    # ----------------------------------------------------

    def build_context(self, results):

        context = []

        for item in results:

            context.append(
                f"""Document : {item['document']}
Page     : {item['page']}

Content:
{item['text']}
"""
            )

        return "\n\n".join(context)

    # ----------------------------------------------------
    # Retrieve Context + Sources
    # ----------------------------------------------------

    def retrieve_context(self, question, top_k=TOP_K_RESULTS):

        results = self.retrieve(question, top_k)

        context = self.build_context(results)

        return context, results


# ==========================================================
# Singleton
# ==========================================================

retriever = Retriever()


# ==========================================================
# Helper Functions
# ==========================================================

def get_context(question, top_k=TOP_K_RESULTS):

    return retriever.retrieve_context(question, top_k)


# ----------------------------------------------------------
# Compatibility Function
# Used by rag_pipeline.py
# ----------------------------------------------------------

def retrieve_documents(question, top_k=TOP_K_RESULTS):

    _, documents = retriever.retrieve_context(question, top_k)

    return documents


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    question = "What is Machine Learning?"

    context, sources = get_context(question)

    print("=" * 80)
    print(context)
    print("=" * 80)
    print(f"Retrieved : {len(sources)}")
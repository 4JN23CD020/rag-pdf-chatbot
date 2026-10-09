"""
=========================================================
PROMPT BUILDER
=========================================================
Creates professional prompts for the Grok LLM.
=========================================================
"""

from backend.config import SYSTEM_PROMPT


class PromptBuilder:

    def __init__(self):

        self.system_prompt = SYSTEM_PROMPT

    # ---------------------------------------------------
    # Build Prompt
    # ---------------------------------------------------

    def build(self, question, documents):

        # Convert retrieved documents into context
        context = ""

        for doc in documents:

            context += f"""
Document : {doc['document']}
Page     : {doc['page']}

Content:
{doc['text']}

----------------------------------------
"""

        prompt = f"""
==================== CONTEXT ====================

{context}

=================================================


==================== QUESTION ===================

{question}

=================================================

Answer ONLY using the document context above.
If the answer is unavailable, reply:

"I couldn't find that information in the uploaded documents."
"""

        return [

            {
                "role": "system",
                "content": self.system_prompt
            },

            {
                "role": "user",
                "content": prompt
            }

        ]


# ==========================================================
# Singleton
# ==========================================================

prompt_builder = PromptBuilder()


# ==========================================================
# Helper Functions
# ==========================================================

def create_prompt(question, documents):

    return prompt_builder.build(question, documents)


# ----------------------------------------------------------
# Compatibility Function
# Used by rag_pipeline.py
# ----------------------------------------------------------

def build_prompt(question, documents):

    return create_prompt(question, documents)


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    sample = [

        {

            "document": "AI.pdf",

            "page": 1,

            "text": "Artificial Intelligence is the simulation of human intelligence."

        }

    ]

    prompt = build_prompt(

        "What is Artificial Intelligence?",

        sample

    )

    print(prompt)
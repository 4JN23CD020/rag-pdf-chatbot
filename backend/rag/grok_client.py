"""
=========================================================
GEMINI CLIENT
=========================================================
Handles communication with Google Gemini.
=========================================================
"""
import os
from google import genai

from backend.config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
)


class GeminiClient:

    def __init__(self):
        if not GEMINI_API_KEY:
            raise ValueError(
                "GEMINI_API_KEY is not configured."
            )

        self.client = genai.Client(
            api_key = os.getenv("GROK_API_KEY")
        )

    def generate(self, messages):

        prompt_parts = []

        for message in messages:

            role = message.get("role", "user").upper()
            content = message.get("content", "")

            prompt_parts.append(
                f"{role}:\n{content}"
            )

        prompt = "\n\n".join(prompt_parts)

        response = self.client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
        )

        if not response or not response.text:
            raise RuntimeError(
                "Gemini returned an empty response."
            )

        return response.text


gemini = GeminiClient()


def ask_grok(messages):
    """
    Kept as ask_grok because the existing RAG pipeline
    already imports this function.
    """

    return gemini.generate(messages)
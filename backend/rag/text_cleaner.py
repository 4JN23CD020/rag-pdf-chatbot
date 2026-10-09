"""
=========================================================
TEXT CLEANER
=========================================================
Cleans extracted PDF text before chunking.
=========================================================
"""

import re


class TextCleaner:

    def __init__(self):
        pass

    # ------------------------------------------
    # Remove extra spaces
    # ------------------------------------------

    def remove_extra_spaces(self, text):

        text = re.sub(r"[ \t]+", " ", text)

        return text.strip()

    # ------------------------------------------
    # Remove empty lines
    # ------------------------------------------

    def remove_empty_lines(self, text):

        lines = text.splitlines()

        cleaned = []

        for line in lines:

            line = line.strip()

            if line != "":

                cleaned.append(line)

        return "\n".join(cleaned)

    # ------------------------------------------
    # Fix broken words
    # ------------------------------------------

    def fix_hyphenated_words(self, text):

        return re.sub(r"-\n", "", text)

    # ------------------------------------------
    # Replace multiple new lines
    # ------------------------------------------

    def normalize_newlines(self, text):

        return re.sub(r"\n{2,}", "\n", text)

    # ------------------------------------------
    # Remove page numbers
    # ------------------------------------------

    def remove_page_numbers(self, text):

        lines = text.split("\n")

        cleaned = []

        for line in lines:

            line = line.strip()

            if line.isdigit():

                continue

            cleaned.append(line)

        return "\n".join(cleaned)

    # ------------------------------------------
    # Remove strange unicode characters
    # ------------------------------------------

    def normalize_unicode(self, text):

        replacements = {

            "“": '"',
            "”": '"',
            "‘": "'",
            "’": "'",
            "•": "-",
            "–": "-",
            "—": "-",
            "\u00A0": " "

        }

        for old, new in replacements.items():

            text = text.replace(old, new)

        return text

    # ------------------------------------------
    # Main Cleaning Function
    # ------------------------------------------

    def clean(self, text):

        text = self.fix_hyphenated_words(text)

        text = self.normalize_unicode(text)

        text = self.remove_page_numbers(text)

        text = self.remove_empty_lines(text)

        text = self.normalize_newlines(text)

        text = self.remove_extra_spaces(text)

        return text


# =====================================================
# Helper Function
# =====================================================

def clean_documents(documents):

    cleaner = TextCleaner()

    cleaned_documents = []

    for document in documents:

        cleaned_documents.append({

            "document": document["document"],

            "page": document["page"],

            "text": cleaner.clean(document["text"])

        })

    return cleaned_documents


# =====================================================
# Testing
# =====================================================

if __name__ == "__main__":

    sample = """

        Python    is   a programming language.


        It is used for AI.


        12

        Deep Learn-
        ing

    """

    cleaner = TextCleaner()

    print(cleaner.clean(sample))
    # =====================================================
# Clean Single Page
# =====================================================

def clean_text(page):

    cleaner = TextCleaner()

    return {

        "document": page["document"],

        "page": page["page"],

        "text": cleaner.clean(page["text"])

    }
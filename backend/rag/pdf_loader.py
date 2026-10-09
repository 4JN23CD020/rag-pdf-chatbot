"""
=========================================================
PDF LOADER
=========================================================
Loads PDF files and extracts text page by page.
=========================================================
"""

import fitz
from pathlib import Path


class PDFLoader:

    def __init__(self, pdf_path):
        self.pdf_path = Path(pdf_path)

    # ----------------------------------------------------
    # Extract every page
    # ----------------------------------------------------

    def extract(self):

        pages = []

        try:

            with fitz.open(self.pdf_path) as document:

                total_pages = len(document)

                for page_number in range(total_pages):

                    page = document.load_page(page_number)

                    text = page.get_text("text")

                    if not text.strip():
                        continue

                    pages.append({

                        "document": self.pdf_path.name,

                        "page": page_number + 1,

                        "text": text.strip()

                    })

        except Exception as e:

            print(f"Error loading {self.pdf_path}: {e}")

            return []

        return pages


# --------------------------------------------------------
# Load Single PDF
# --------------------------------------------------------

def load_pdf(pdf_path):

    loader = PDFLoader(pdf_path)

    return loader.extract()


# --------------------------------------------------------
# Load Multiple PDFs
# --------------------------------------------------------

def load_all_pdfs(folder):

    folder = Path(folder)

    documents = []

    pdf_files = sorted(folder.glob("*.pdf"))

    for pdf in pdf_files:

        pages = load_pdf(pdf)

        documents.extend(pages)

        print(f"Loaded : {pdf.name}")

    return documents


# --------------------------------------------------------
# Testing
# --------------------------------------------------------

if __name__ == "__main__":

    from backend.config import UPLOAD_DIR

    data = load_all_pdfs(UPLOAD_DIR)

    print(f"\nPages Loaded : {len(data)}")

    for page in data[:5]:

        print("-" * 60)

        print(page["document"])

        print(page["page"])

        print(page["text"][:300])
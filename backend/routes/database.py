"""
=========================================================
DATABASE ROUTES
=========================================================
Manage uploaded PDFs and FAISS database.
=========================================================
"""

import os
import shutil

from fastapi import APIRouter

from backend.config import (
    UPLOAD_DIR,
    VECTOR_DB_DIR
)

from backend.rag.vector_store import (
    database_stats,
    reset_database
)

router = APIRouter(
    prefix="/database",
    tags=["Database"]
)


# ---------------------------------------------------------
# Database Status
# ---------------------------------------------------------

@router.get("/status")
def status():

    pdfs = []

    if UPLOAD_DIR.exists():

        pdfs = [

            file.name

            for file in UPLOAD_DIR.glob("*.pdf")

        ]

    stats = database_stats()

    return {

        "uploaded_documents": len(pdfs),

        "documents": pdfs,

        "vectors": stats["vectors"]

    }


# ---------------------------------------------------------
# Reset Database
# ---------------------------------------------------------

@router.delete("/reset")
def reset():

    # Delete uploaded PDFs

    if UPLOAD_DIR.exists():

        shutil.rmtree(UPLOAD_DIR)

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    # Reset FAISS database

    reset_database()

    return {

        "status": "success",

        "message": "Database reset successfully."

    }
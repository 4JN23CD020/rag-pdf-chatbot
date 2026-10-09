"""
==========================================================
UPLOAD ROUTE
==========================================================
"""

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse

from pathlib import Path
import shutil

from backend.config import *

from backend.rag.rag_pipeline import process_pdf

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


# ----------------------------------------------------------
# Upload PDF(s)
# ----------------------------------------------------------

@router.post("/")

async def upload_pdf(files: list[UploadFile] = File(...)):

    uploaded_files = []

    for file in files:

        extension = Path(file.filename).suffix.lower()

        if extension not in ALLOWED_EXTENSIONS:
            
            return JSONResponse(
            status_code=400,
            content={
                "status": "error",
                "message": f"{file.filename} is not a PDF."
        }
    )

        save_path = UPLOAD_DIR / file.filename

        with open(save_path, "wb") as buffer:
            if save_path.exists():
                continue

            shutil.copyfileobj(file.file, buffer)

        process_pdf(save_path)

        uploaded_files.append(file.filename)

    return JSONResponse(
        {
            "status": "success",
            "uploaded_files": uploaded_files,
            "total_uploaded": len(uploaded_files)
        }
    )


# ----------------------------------------------------------
# List Uploaded PDFs
# ----------------------------------------------------------

@router.get("/list")

def list_documents():

    pdfs = []

    for file in UPLOAD_DIR.glob("*.pdf"):

        pdfs.append(file.name)

    return {

        "documents": pdfs,

        "count": len(pdfs)

    }


# ----------------------------------------------------------
# Delete PDF
# ----------------------------------------------------------

@router.delete("/{filename}")

def delete_document(filename: str):

    file_path = UPLOAD_DIR / filename

    if file_path.exists():

        file_path.unlink()

        return {

            "status": "Deleted",

            "file": filename

        }

    return {

        "status": "File Not Found"

    }
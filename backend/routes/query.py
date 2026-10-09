"""
=========================================================
QUERY ROUTE
=========================================================
Handles user questions.
=========================================================
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from backend.rag.rag_pipeline import generate_answer


router = APIRouter(
    prefix="/query",
    tags=["Query"]
)


class QueryRequest(BaseModel):
    question: str


@router.post("/")
async def query(request: QueryRequest):

    question = request.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    try:

        result = generate_answer(question)

        return {
            "status": "success",
            "question": question,
            "answer": result["answer"],
            "sources": result["sources"]
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
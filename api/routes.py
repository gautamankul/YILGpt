from fastapi import APIRouter, HTTPException
from services.rag_service import process_query

router = APIRouter()

@router.post("/query")
async def query_endpoint(request: dict):
    try:
        question = request.get("question")

        if not question:
            raise HTTPException(status_code=400, detail="Question is required")

        response = process_query(question)

        return {"answer": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
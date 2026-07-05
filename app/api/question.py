from fastapi import APIRouter, HTTPException

from app.config.settings import settings
from app.schemas.question import QuestionRequest
from app.schemas.response import AnswerResponse
from app.services.qa_service import QAService

router = APIRouter()

qa_service = QAService(settings.VECTOR_STORE_PATH)


@router.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):

    try:
        return qa_service.answer_question(request.question)

    except FileNotFoundError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Failed to process the question."
        )

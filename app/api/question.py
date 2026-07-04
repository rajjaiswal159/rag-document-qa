from fastapi import APIRouter, HTTPException
from app.exceptions import VectorStoreNotFoundError
from app.schemas.question import QuestionRequest
from app.services.qa_service import QAService
from app.config.settings import settings
from app.schemas.response import AnswerResponse

router = APIRouter()


@router.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):

    try:
        qa_service = QAService(settings.VECTOR_STORE_PATH)

        return qa_service.answer_question(request.question)

    except VectorStoreNotFoundError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )
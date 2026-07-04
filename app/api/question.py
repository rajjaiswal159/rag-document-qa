from fastapi import APIRouter

from app.schemas.question import QuestionRequest
from app.services.qa_service import QAService
from app.config.settings import settings

router = APIRouter()


@router.post("/ask")
def ask_question(request: QuestionRequest):

    qa_service = QAService(settings.VECTOR_STORE_PATH)

    return qa_service.answer_question(request.question)
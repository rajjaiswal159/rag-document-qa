from fastapi import APIRouter, HTTPException
from app.config.settings import settings
from app.schemas.question import QuestionRequest
from app.schemas.response import AnswerResponse
from app.services.qa_service import QAService
from app.utils.logger import logger
from app.services.cleanup_service import CleanupService

router = APIRouter(
    prefix="/ask",
    tags=["ask"]
)

cleanup_service = CleanupService()
qa_service = QAService()


@router.post("/", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):

    try:
        cleanup_service.cleanup_expired()

        return qa_service.answer_question(
            request.document_id,
            request.question
        )

    except FileNotFoundError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

    except Exception:
        logger.exception("Unexpected error while processing question.")

        raise HTTPException(
            status_code=500,
            detail="Failed to process the question."
        )

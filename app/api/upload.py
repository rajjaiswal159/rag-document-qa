from fastapi import APIRouter, File, HTTPException, UploadFile
from app.utils.logger import logger
from app.services.file_service import save_pdf
from app.services.indexing_service import IndexingService
from app.services.cleanup_service import CleanupService
from app.services.document_service import DocumentService

document_service = DocumentService()
indexing_service = IndexingService()
cleanup_service = CleanupService()

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post("/")
def upload_pdf(file: UploadFile = File(...)):
    try:

        cleanup_service.cleanup_expired()
        
        # Save the uploaded PDF
        file_path = save_pdf(file)

        # Index the uploaded document
        document_id = indexing_service.index_document(file_path)

        # Save document metadata
        document_service.add_document(
            document_id=document_id,
            filename=file.filename
        )

        return {
            "message": "File uploaded successfully.",
            "document_id": document_id,
            "filename": file.filename
        }

    except HTTPException:
        # Re-raise HTTP exceptions from lower layers
        raise

    except Exception:
        logger.exception("Unexpected error during PDF upload.")

        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred."
        )
        
    finally:
        if file_path and file_path.exists():
            file_path.unlink()

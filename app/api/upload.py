from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.file_service import save_pdf
from app.services.indexing_service import IndexingService

indexing_service = IndexingService()

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post("/")
def upload_pdf(file: UploadFile = File(...)):
    try:
        # Save the uploaded PDF
        file_path = save_pdf(file)

        # Index the uploaded document
        indexing_service.index_document(str(file_path))

        return {
            "message": "File uploaded successfully.",
            "filename": file.filename
        }

    except HTTPException:
        # Re-raise HTTP exceptions from lower layers
        raise

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred."
        )
        
    finally:
        if file_path and file_path.exists():
            file_path.unlink()

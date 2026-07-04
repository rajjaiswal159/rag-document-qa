from fastapi import APIRouter, UploadFile, File

from app.services.file_service import save_pdf
from app.services.indexing_service import IndexingService

indexing_service = IndexingService()

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post("/")
def upload_pdf(file: UploadFile = File(...)):
    
    file_path = save_pdf(file)

    indexing_service.index_document(str(file_path))

    return {
        "message": "File uploaded successfully.",
        "filename": file.filename,
        "path": str(file_path)
    }
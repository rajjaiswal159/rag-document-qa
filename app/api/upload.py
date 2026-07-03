from fastapi import APIRouter, UploadFile, File

from app.services.file_service import save_pdf

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post("/")
def upload_pdf(file: UploadFile = File(...)):
    file_path = save_pdf(file)

    return {
        "message": "File uploaded successfully.",
        "filename": file.filename,
        "path": str(file_path)
    }
from pathlib import Path
import shutil
from fastapi import UploadFile, HTTPException
import uuid
from fastapi import UploadFile, HTTPException
from app.utils.logger import logger
from app.config.settings import settings

# Upload directory
UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def save_pdf(file: UploadFile) -> Path:

    # Validate file extension
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    # Validate MIME type
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Only PDF files are allowed."
        )

    unique_filename = f"{uuid.uuid4()}.pdf"

    file_path = UPLOAD_DIR / unique_filename

    try:
        content = file.file.read()

        if len(content) > settings.MAX_FILE_SIZE:
            raise HTTPException(
                status_code=400,
                detail="File size exceeds the allowed limit."
            )
        
        with open(file_path, "wb") as buffer:
            buffer.write(content)

        logger.info(
            "File uploaded successfully: %s -> %s",
            file.filename,
            unique_filename
        )

        return file_path

    except HTTPException:
        raise

    except Exception:
        logger.exception("Failed to save uploaded file.")
    
        raise HTTPException(
            status_code=500,
            detail="Failed to save file."
        )
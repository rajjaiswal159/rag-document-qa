from pathlib import Path
import uuid

from fastapi import UploadFile, HTTPException

from app.config.settings import settings
from app.utils.logger import logger

# Directory for storing uploaded PDF files
UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def save_pdf(file: UploadFile) -> Path:

    # Ensure the uploaded file has a .pdf extension
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    # Ensure the uploaded file has the correct MIME type
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Only PDF files are allowed."
        )

    # Generate a unique filename to avoid conflicts
    unique_filename = f"{uuid.uuid4()}.pdf"

    file_path = UPLOAD_DIR / unique_filename

    try:
        # Read the uploaded file
        content = file.file.read()

        # Validate the file size
        if len(content) > settings.MAX_FILE_SIZE:
            raise HTTPException(
                status_code=400,
                detail="File size exceeds the allowed limit."
            )

        # Save the file to disk
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
        logger.exception("Failed to save uploaded file: %s", file.filename)

        raise HTTPException(
            status_code=500,
            detail="Failed to save file."
        )
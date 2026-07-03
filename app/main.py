from fastapi import FastAPI
from app.config.settings import settings

app = FastAPI(
    title="Document QA API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Document QA API is running",
        "max_file_size": settings.MAX_FILE_SIZE
    }
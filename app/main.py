from fastapi import FastAPI
from app.db.database import Base, engine
from app.db import models
from app.api.question import router as question_router
from app.api.upload import router as upload_router

# Create the FastAPI application
app = FastAPI(
    title="Document QA API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

# Register API routes
app.include_router(upload_router)
app.include_router(question_router)


@app.get("/")
def home():
    # Health check endpoint
    return {
        "message": "Document QA API is running"
    }
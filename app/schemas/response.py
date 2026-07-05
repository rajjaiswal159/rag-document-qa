from pydantic import BaseModel


# Source information for a retrieved document
class Source(BaseModel):
    source: str
    page: int


# API response model for question answering
class AnswerResponse(BaseModel):
    answer: str
    sources: list[Source]
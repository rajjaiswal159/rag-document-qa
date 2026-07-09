from pydantic import BaseModel


# Request model for user questions
class QuestionRequest(BaseModel):
    document_id: str
    question: str
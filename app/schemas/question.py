from pydantic import BaseModel


# Request model for user questions
class QuestionRequest(BaseModel):
    question: str
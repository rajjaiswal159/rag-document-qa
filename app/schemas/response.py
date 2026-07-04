from pydantic import BaseModel


class Source(BaseModel):
    source: str
    page: int


class AnswerResponse(BaseModel):
    answer: str
    sources: list[Source]
from pydantic import BaseModel
from sqlmodel import Field, SQLModel


class ExternalReview(BaseModel):
    text: str
    rating: int
    author: str


class ReviewTable(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content: str
    score: int
    reviewer_name: str
    label: str | None = None

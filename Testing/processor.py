from pydantic import BaseModel, Field


class Review(BaseModel):
    text: str = Field(min_length=5)
    score: int = Field(ge=0, le=5)


def calculate_utility(review: Review) -> bool:
    return len(review.text) > 10 and review.score > 3

import datetime
import uuid
from typing import Annotated, Any

from google_play_scraper import Sort, reviews
from prefect import task
from pydantic import BaseModel, BeforeValidator, Field
from rich import print


def cast_to_uuid(v: str | uuid.UUID) -> uuid.UUID:
    if isinstance(v, str):
        return uuid.UUID(v)
    return v


UUID_TYPE = Annotated[uuid.UUID, BeforeValidator(cast_to_uuid)]
type ReviewPayload = tuple[list[dict[str, Any]], Any]


class Review(BaseModel):
    reviewId: UUID_TYPE
    at: datetime.datetime

    content: str = Field(min_length=1)
    score: int = Field(ge=1, le=5)
    thumbsUpCount: int


@task
def ingest_data(app_id: str) -> ReviewPayload:
    payload = reviews(
        app_id,
        lang="en",
        country="us",
        sort=Sort.NEWEST,
        count=1,
    )

    return payload


review, continuation_token = ingest_data("com.JindoBlu.OfflineGames")

review_model = Review.model_validate(review[0])
print(review_model.reviewId, type(review_model.reviewId))

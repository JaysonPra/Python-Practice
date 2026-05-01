from database import engine
from logging_config import setup_logger
from loguru import logger
from models import Review
from sqlmodel import Session

setup_logger()


def add_review(reviews: list[dict]) -> None:
    with Session(engine) as session:
        for i, review_dict in enumerate(reviews):
            try:
                validated_review = Review.model_validate(review_dict)
                session.add(validated_review)
                logger.success(f"Review {i} added successfully!")
            except Exception as e:
                logger.critical(f"Failed to add review {i}: {e}")

        try:
            session.commit()
            logger.success("Transaction committed successfully!")
        except Exception as e:
            session.rollback()
            logger.critical(f"Database commit failed: {e}")


raw_data = [
    {"text": "Amazing review!", "sentiment": "positive", "score": 0.95},
    {"text": "Terrible...", "sentiment": "negative"},
    {"text": 12345, "sentiment": "neutral", "score": "high"},
    {"text": "Okay", "sentiment": "neutral", "score": 0.5},
]
add_review(raw_data)

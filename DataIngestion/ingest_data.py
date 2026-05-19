from logging_config import setup_logger
from loguru import logger
from models import Review
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import Session

setup_logger()


def add_review(reviews: list[dict], session: Session) -> None:
    valid_review_count = 0

    for i, review_dict in enumerate(reviews):
        try:
            validated_review = Review.model_validate(review_dict)
            session.add(validated_review)
            valid_review_count += 1

        except ValidationError:
            logger.warning(f"Skipping index {i} due to invalid schema.")

    if valid_review_count == 0:
        logger.info("No valid reviews to commit")
        return

    try:
        session.commit()
        logger.success(
            f"Successfully committed {valid_review_count} reviews to the database!"
        )

    except SQLAlchemyError:
        session.rollback()
        logger.exception("Database transaction failed to commit. Rolled back.")

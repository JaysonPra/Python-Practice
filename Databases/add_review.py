from loguru import logger
from postresql_imp import Review, engine
from sqlmodel import Session


def add_review():
    new_review = Review(
        text="This product is amazing!", source_api="Amazon_v1", label="High Utility"
    )

    with Session(engine) as session:
        session.add(new_review)
        session.commit()
        session.refresh(new_review)

        logger.success(f"Review saved with ID: {new_review.id}")


if __name__ == "__main__":
    add_review()

from models import ExternalReview, ReviewTable
from sqlmodel import Session, create_engine

engine = create_engine("sqlite://")  # Placeholder for actual database connection


def ingest_review(api_data: dict, label: str | None = None):
    external_data = ExternalReview(**api_data)

    db_review = ReviewTable(
        content=external_data.text,
        score=external_data.rating,
        reviewer_name=external_data.author,
        label=label,
    )

    with Session(engine) as session:
        session.add(db_review)
        session.commit()

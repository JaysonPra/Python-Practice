import pytest
from ingest_data import add_review
from models import Review as Review  # noqa: F401
from sqlmodel import Session, SQLModel, create_engine, func, select


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


# -- Helper --


def _get_count(session):
    """Returns the total number of reviews in the database."""
    return session.exec(select(func.count()).select_from(Review)).one()


# -- Test --


def test_add_single_valid_review(session):
    valid_data = [{"text": "Amazing review!", "sentiment": "positive", "score": 0.95}]

    add_review(valid_data, session)

    count = _get_count(session)
    assert count == 1


def test_add_multiple_valid_reviews(session):
    valid_data = [
        {
            "text": "Very nice product! I love it!",
            "sentiment": "positive",
            "score": 0.94,
        },
        {
            "text": "Product needs more time in the oven. It's not ready for the public.",
            "sentiment": "negative",
            "score": 0.89,
        },
        {
            "text": "Pretty good. I have some gripes about it, but overall I like it.",
            "sentiment": "positiv",
            "score": 0.77,
        },
    ]

    add_review(valid_data, session)

    count = _get_count(session)
    assert count == 3


def test_missing_required_fields(session):
    missing_data = [{"text": "It's fine. I like it...", "sentiment": "positive"}]

    add_review(missing_data, session)

    count = _get_count(session)
    assert count == 0


def test_add_invalid_data_types(session):
    invalid_data = [{"text": 12345, "sentiment": "neutral", "score": "high"}]

    add_review(invalid_data, session)

    count = _get_count(session)
    assert count == 0

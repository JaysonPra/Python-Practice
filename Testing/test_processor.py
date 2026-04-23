import pytest
from processor import Review, calculate_utility
from pydantic import ValidationError


def test_valid_review_parsing():
    """Test that a normal review passes verification"""
    data = {"text": "Hello, how are you doing?", "score": 4}
    review = Review(**data)
    assert review.score == 4


def test_invalid_review_too_short():
    """Test that Pydantic catches the crash due to Validation Error"""
    with pytest.raises(ValidationError):
        Review(text="Hi", score=5)


@pytest.mark.parametrize(
    "text, score, expected",
    [
        ("This is a very long review that should be useful!", 5, True),
        ("Small!", 1, False),
        ("This is a very long review that is useless!", 2, False),
    ],
)
def test_utility_logic(text, score, expected):
    """Test logic using"""
    review = Review(text=text, score=score)
    assert calculate_utility(review) == expected

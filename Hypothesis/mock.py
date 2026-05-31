from hypothesis import given
from hypothesis import strategies as st


def reverse(input_str: str) -> str:
    return input_str[::-1]


@given(st.text())
def test_reverse(input_str: str) -> None:
    assert (reverse(reverse(input_str))) == input_str

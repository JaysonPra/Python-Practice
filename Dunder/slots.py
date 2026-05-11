class ReviewSlots:
    __slots__ = ("text", "score", "is_spam")

    def __init__(self, text: str, score: float, is_spam: bool) -> None:
        self.text = text
        self.score = score
        self.is_spam = is_spam


class ReviewBase:
    def __init__(self, text: str, score: float, is_spam: bool) -> None:
        self.text = text
        self.score = score
        self.is_spam = is_spam

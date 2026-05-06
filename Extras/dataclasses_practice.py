import inspect
from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class ModelCard:
    model_name: str
    version: int
    accuracy: float
    created_at: datetime = field(default_factory=datetime.now, init=False)

    is_production_ready: bool = field(init=False)

    def __post_init__(self) -> None:
        if not (0 <= self.accuracy <= 1):
            raise ValueError("Accuracy must be between 0 and 1")

        object.__setattr__(self, "is_production_ready", self.accuracy > 0.9)

    def __str__(self) -> str:
        doc = f"""
            Model: {self.model_name}
            Version: {self.version}
            Accuracy: {self.accuracy}
            Created At: {self.created_at}
            Production Ready: {"Ready" if self.is_production_ready else "Not Ready"}
        """

        return inspect.cleandoc(doc)


test = ModelCard(model_name="XGBoost", version=1, accuracy=0.95)

print(test)

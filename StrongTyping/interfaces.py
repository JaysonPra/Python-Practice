from typing import Protocol


class Predictor(Protocol):
    def predict(self, data: list[float]) -> float: ...


class XGBoostClassifier:
    def predict(self, data: list[float]) -> float:
        return 0.85


class LogisticRegression:
    def predict(self, data: list[float]) -> float:
        return 0.70


def run_inference(model: Predictor, data: list[float]):
    return model.predict(data)


run_inference(XGBoostClassifier(), [1.0, 2.0])
run_inference(LogisticRegression(), [5.0, 1.5])

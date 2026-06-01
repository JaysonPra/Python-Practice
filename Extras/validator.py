from dataclasses import dataclass
from typing import Any, Protocol


class ValidationRule(Protocol):
    def validate(self, data: dict[str, Any]) -> bool: ...

    @property
    def error_message(self) -> str: ...


@dataclass(frozen=True)
class CheckMissing:
    field: str

    def validate(self, data: dict[str, Any]) -> bool:
        return self.field in data and data[self.field] is not None

    @property
    def error_message(self) -> str:
        return f"Missing required field: '{self.field}'"


@dataclass(frozen=True)
class CheckType:
    field: str
    expected_type: type

    def validate(self, data: dict[str, Any]) -> bool:
        if self.field not in data:
            return False

        return isinstance(data[self.field], self.expected_type)

    @property
    def error_message(self) -> str:
        return f"Field '{self.field} must be of type {self.expected_type.__name__}"


class DataValidator:
    def __init__(self) -> None:
        self._rules: list[ValidationRule] = []

    def add_rule(self, rule: ValidationRule) -> None:
        self._rules.append(rule)

    def verify(self, data: dict[str, Any]) -> list[str]:
        errors: list[str] = []

        for rule in self._rules:
            if not rule.validate(data):
                errors.append(rule.error_message)

        return errors


if __name__ == "__main__":
    validation_suite = DataValidator()

    validation_suite.add_rule(CheckMissing("num_rooms"))
    validation_suite.add_rule(CheckType("num_rooms", int))
    validation_suite.add_rule(CheckMissing("booked"))
    validation_suite.add_rule(CheckType("booked", bool))

    corrupt_dict: dict[str, Any] = {"num_rooms": "4"}
    errors = validation_suite.verify(corrupt_dict)
    for error in errors:
        print(error)

    print("-" * 40)

    correct_dict: dict[str, Any] = {"num_rooms": 4, "booked": True}
    errors = validation_suite.verify(correct_dict)
    for error in errors:
        print(error)

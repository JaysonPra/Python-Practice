from typing import Any, Callable, Generic, TypeVar

T = TypeVar("T", int, float)


class Verified(Generic[T]):
    def __init__(self, validator: Callable[[T], bool]) -> None:
        self.validator = validator
        self.name = ""

    def __set_name__(self, owner: Any, name: str) -> None:
        self.name = name

    def __get__(self, instance, owner) -> Any:
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value) -> None:
        if not self.validator(value):
            raise ValueError(f"Invalid value for {self.name}: {value}")
        instance.__dict__[self.name] = value


class ModelConfig:
    lr = Verified(lambda x: 0 < x < 1)
    batch_size = Verified(lambda x: x > 0)


config = ModelConfig()
config.lr = 0.5
config.batch_size = 32

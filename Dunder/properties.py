class ModelConfig:
    def __init__(self) -> None:
        self._lr = 0.5
        self._batch_size = 32

    @property
    def lr(self) -> float:
        return self._lr

    @lr.setter
    def lr(self, value: float) -> None:
        if not (0 < value < 1):
            raise ValueError(f"Invalid value for lr: {value}")
        self._lr = value

    @property
    def batch_size(self) -> int:
        return self._batch_size

    @batch_size.setter
    def batch_size(self, value: int) -> None:
        if value <= 0:
            raise ValueError(f"Invalid value for batch_size: {value}")
        self._batch_size = value


config = ModelConfig()
config.lr = 0.5
config.batch_size = 32

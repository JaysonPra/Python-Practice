from contextlib import ContextDecorator
from time import perf_counter

import numpy as np


class Timer(ContextDecorator):
    def __init__(self, task_name: str | None = None) -> None:
        self.task_name = task_name

    def __enter__(self):
        self.start_time = perf_counter()
        if self.task_name:
            print(f"Started task: {self.task_name}.")

        return self

    def __exit__(self, exc_type, exc, tb):
        total_time = perf_counter() - self.start_time

        if self.task_name:
            print(f"Finished task: {self.task_name}.")
        print(f"Total time taken: {total_time}")

        if exc_type:
            print(f"Task failed with error: {exc_type}")

        return None


with Timer():
    np.random.randint(1, 100, (5000, 5000))

with Timer("Creation of random array"):
    np.random.randint(1, 100, (5000, 5000))


@Timer("Creation of random array")
def main() -> None:
    np.random.randint(1, 100, (5000, 5000))


if __name__ == "__main__":
    main()

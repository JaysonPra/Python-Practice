from time import perf_counter

import numpy as np


class Timer:
    def __init__(self, task_name: str) -> None:
        self.task_name = task_name

    def __enter__(self):
        self.start_time = perf_counter()
        print(f"Started Task: {self.task_name}...")

        return self

    def __exit__(self, exc_type, exc, tb):
        self.end_time = perf_counter()
        total_time = self.end_time - self.start_time

        print(f"Finished Task: {self.task_name}. Took {total_time:.4f} seconds")

        if exc_type:
            print(f"Task failed with error: {exc_type}")

        return False


with Timer("Creation of random numpy array"):
    random_arr = np.random.randint(1, 100, size=(5000, 5000))

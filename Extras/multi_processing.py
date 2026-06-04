import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from typing import Any, Callable


def timer(func: Callable[..., Any]):
    def wrapper(*args: Any, **kwargs: dict[Any, Any]):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        print(f"Time: {(end_time - start_time):.4f} seconds")

        return result

    return wrapper


def cpu_bound_task(n: int) -> int:
    count: int = 0

    for _ in range(n):
        count += 1

    return count


@timer
def run_with_threads(n: int, iterations: int) -> list[int]:
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(cpu_bound_task, n) for _ in range(iterations)]
        return [f.result() for f in futures]


@timer
def run_with_processes(n: int, iterations: int) -> list[int]:
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(cpu_bound_task, n) for _ in range(iterations)]
        return [f.result() for f in futures]


if __name__ == "__main__":
    n = 10_000_000
    iterations = 4

    print("Starting threaded execution...")
    run_with_threads(n, iterations)

    print("\nStarting multi-process execution...")
    run_with_processes(n, iterations)

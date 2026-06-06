import random
import time
from collections.abc import Callable
from typing import Any


def flaky_api_call(attempt_tracker: list[int], endpoint: str) -> str:
    attempt_tracker.append(1)

    if len(attempt_tracker) < 4:
        raise ConnectionError(f"Timeout on {endpoint}")

    return f"SUCCESS from {endpoint}"


def execute_with_retry(
    func: Callable[..., Any],
    max_retries: int = 5,
    base_delay: float = 0.5,
    *args: Any,
    **kwargs: Any,
) -> Any:
    for attempt in range(max_retries):
        try:
            return func(*args, **kwargs)
        except ConnectionError as e:
            print(e)
            if attempt == max_retries - 1:
                raise e

            delay = (base_delay * (2 * attempt)) + random.uniform(0.1, 0.5)
            time.sleep(delay)


if __name__ == "__main__":
    tracker: list[int] = []
    target_url = "https://api.production.internal/v1/data"

    result = execute_with_retry(flaky_api_call, 5, 0.5, tracker, target_url)

    print(result)

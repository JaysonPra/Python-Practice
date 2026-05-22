import random
import time
from contextlib import contextmanager
from dataclasses import dataclass

from loguru import logger
from pydantic import BaseModel, Field, ValidationError

POSITIVE_SENTIMENT_SCORE = 15.0

logger.add(
    "logs/{time:YYYY-MM-DD}.log",
    serialize=True,
    rotation="10 MB",
    retention="5 days",
    compression="zip",
    level="TRACE",
)


@dataclass
class TimerMetrics:
    duration_ms: float = 0.0


@contextmanager
def track_latency():
    metrics = TimerMetrics()
    start_time = time.perf_counter()

    try:
        yield metrics
    finally:
        end_time = time.perf_counter()
        metrics.duration_ms = (end_time - start_time) * 1000


class Payload(BaseModel):
    user_id: str = Field(pattern=r"^user_[0-9]+$")
    text: str = Field(min_length=1)


def validate_payload(payload: dict[str, str]) -> Payload | None:
    try:
        return Payload.model_validate(payload)

    except ValidationError as e:
        logger.error(f"Failed to validate schema: {e}")
        return None


def generate_mock_embeddings(payload: Payload) -> list[float]:
    logger.info(f"Generating embeddings for user {payload.user_id}")

    time.sleep(random.choice([0.01, 0.02, 0.05]))

    words = payload.text.split()
    mock_vector = [float(len(words)), float(len(payload.text)), 0.891]

    return mock_vector


def sentiment_scorer(vector: list[float]) -> str:
    vector_sum = sum(vector)

    if vector_sum > POSITIVE_SENTIMENT_SCORE:
        return "Positive"
    else:
        return "Negative"


def show_summary_report(
    total_processed: int, total_errors: int, latency_history: list[float]
) -> None:
    logger.debug("\n--- FINAL METRICS REPORT ---")

    logger.info(f"Total Successful Rows: {total_processed}")
    logger.info(f"Total Failed Rows: {total_errors}")

    if latency_history:
        sorted_latencies = sorted(latency_history)
        mid_index = len(sorted_latencies) // 2
        p50_latency = sorted_latencies[mid_index]
        logger.info(f"p50 Pipeline Latency: {p50_latency:.4f} ms")
    else:
        logger.info("p50 Pipeline Latency: 0.0000 ms")


def run_entire_pipeline(payloads: list[dict[str, str]]) -> None:
    total_processed: int = 0
    total_errors: int = 0
    latency_history: list[float] = []

    logger.debug("--- PIPELINE STARTING ---")

    for item in payloads:
        with track_latency() as timer:
            validated_item = validate_payload(item)

            if validated_item is None:
                total_errors += 1
                continue

            mock_vector = generate_mock_embeddings(validated_item)

            sentiment = sentiment_scorer(mock_vector)

            logger.success(
                f"User {item['user_id']} sentiment: {sentiment} (Vector: {mock_vector})"
            )

        total_processed += 1
        latency_history.append(timer.duration_ms)

    show_summary_report(total_processed, total_errors, latency_history)
    logger.debug("--- PIPELINE FINISHED ---")


if __name__ == "__main__":
    raw_incoming_data = [
        {
            "user_id": "user_101",
            "text": "This new machine learning framework is absolutely incredible!",
        },
        {"user_id": "user_102", "text": ""},
        {"invalid_key": "corrupted"},
        {"user_id": "user_103", "text": "Short text."},
        {
            "user_id": "user_104",
            "text": "Designing machine learning systems requires strict data contracts and latency metrics.",
        },
    ]

    run_entire_pipeline(raw_incoming_data)

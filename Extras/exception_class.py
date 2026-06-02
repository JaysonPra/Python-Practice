from typing import Any

from loguru import logger


class MLSystemError(Exception):
    pass


class DataPipelineError(MLSystemError):
    pass


class ModelLoadError(MLSystemError):
    pass


def run_inference_pipeline(data: dict[str, Any]) -> None:
    try:
        raw_features = data["features"]
    except KeyError as error:
        raise DataPipelineError(
            "Inference pipeline failed: Missing required input features."
        ) from error

    print(raw_features)


if __name__ == "__main__":
    payload = {"metadata": {"timestamp": 1515}}

    try:
        run_inference_pipeline(payload)
    except MLSystemError as error:
        logger.error(f"Caught exception: {error}")

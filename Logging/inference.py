import argparse

from logger_config import setup_logging
from loguru import logger

setup_logging()


def run_classifier(review_text: str):
    logger.trace(f"Incoming raw text length: {len(review_text)}")

    try:
        logger.info("Starting inference")

        prediction = "High Utility"

        logger.success(f"Prediction complete: {prediction}")

        return prediction

    except Exception as e:
        logger.error(f"Inference failed: {e}")
        raise


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--text", required=True, help="The string to classify", type=str
    )

    args = parser.parse_args()

    run_classifier(args.text)

from loguru import logger


def setup_logger() -> None:
    logger.add("logs/{time:YYYY-MM-DD}.json", serialize=True, level="DEBUG")

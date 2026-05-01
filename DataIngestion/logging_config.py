from loguru import logger


def setup_logger() -> None:
    logger.add("logs/{time:YYYY-MM-DD-HH-mm-ss}.json", serialize=True, level="TRACE")

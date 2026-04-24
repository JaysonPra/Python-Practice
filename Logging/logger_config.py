from loguru import logger


def setup_logging():
    logger.add(
        "logs/{time:YYYY-MM-DD-HH-mm-ss}.log",
        serialize=True,
        rotation="10 MB",
        retention="5 days",
        compression="zip",
        level="TRACE",
    )

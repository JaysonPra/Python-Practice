from loguru import logger


def setup_logging():
    logger.add(
        "logs/system_trace.json",
        serialize=True,
        rotation="10 MB",
        retention="5 days",
        compression="zip",
        level="TRACE",
    )

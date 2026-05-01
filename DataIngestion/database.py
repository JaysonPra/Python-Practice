from typing import cast

from logging_config import setup_logger
from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlmodel import Session, SQLModel, create_engine, select, text

setup_logger()


class Settings(BaseSettings):
    database_url: str = cast(str, None)

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()

engine = create_engine(settings.database_url)

try:
    with Session(engine) as session:
        session.exec(select(text("1")))
        logger.success("Engine created successfully!")
except Exception as e:
    logger.critical(f"Failed to create engine: {e}")


def init_db():
    try:
        SQLModel.metadata.create_all(engine)
        logger.success("Database tables created successfully!")
    except Exception as e:
        logger.critical(f"Failed to create tables: {e}")


init_db()

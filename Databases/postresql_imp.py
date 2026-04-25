from sqlmodel import Field, SQLModel, create_engine


class Review(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, gt=0)
    text: str
    label: str | None = None
    source_api: str


db_url = "postgresql+psycopg://dev_user:dev_password@localhost:5432/review_db"
engine = create_engine(db_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    create_db_and_tables()
    print("Database is ready for reviews!")

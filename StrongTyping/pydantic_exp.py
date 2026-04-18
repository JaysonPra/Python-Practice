from pydantic import BaseModel, Field, PositiveInt


class User(BaseModel):
    id: PositiveInt
    Name: str = Field(min_length=2)
    age: PositiveInt


user = User(id=123, Name="Jayson Pradhananga", age=21)

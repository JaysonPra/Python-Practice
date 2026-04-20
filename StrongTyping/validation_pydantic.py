from pydantic import BaseModel, Field, field_validator


class Product(BaseModel):
    price: float
    discount: int = Field(ge=0, lt=100)

    @field_validator("price")
    @classmethod
    def price_must_be_positive(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("Price must be positive")
        return v


product1 = Product(price=-1.5, discount=50)

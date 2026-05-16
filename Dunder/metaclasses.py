class RequireTableConfig(type):
    def __new__(mcs, name, bases, namespace):
        if bases and "__tablename__" not in namespace:
            raise TypeError(f"Database model {name!r} must define a '__tablename__'")

        return super().__new__(mcs, name, bases, namespace)


class BaseModel(metaclass=RequireTableConfig): ...


class User(BaseModel):
    __tablename__ = "user"


d1 = User()

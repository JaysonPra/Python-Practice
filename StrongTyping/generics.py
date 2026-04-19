from typing import Generic, TypeVar

T = TypeVar("T")


class DataBuffer(Generic[T]):
    def __init__(self):
        self.__data: list[T] = []

    def push(self, item: T) -> None:
        self.__data.append(item)

    def pop(self) -> T:
        return self.__data.pop()


# A Generic in Python with a type is more of a suggestion - meaning it is not enforced
int_buffer = DataBuffer[int]()
int_buffer.push(1)
popped_int = int_buffer.pop()
print(f"The popped number: {popped_int} | The type of the number: {type(popped_int)}")

# I can still push a floating point number to the buffer
int_buffer.push(3.54)
popped_float = int_buffer.pop()
print(
    f"The popped number: {popped_float} | The type of the number: {type(popped_float)}"
)

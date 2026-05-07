from typing import Generator, Self


class CountDown:
    def __init__(self, count: int) -> None:
        self.count = count

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> int:
        if self.count <= 0:
            raise StopIteration

        number = self.count
        self.count -= 1
        return number


class CountDownWithIter:
    def __init__(self, count: int) -> None:
        self.count = count

    def __iter__(self) -> Generator[int]:
        current = self.count
        while current > 0:
            yield current
            current -= 1


for i in CountDown(3):
    print(i)

for i in CountDownWithIter(3):
    print(i)

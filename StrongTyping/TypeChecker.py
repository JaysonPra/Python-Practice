from typing import Literal, TypeIs

type Direction = Literal["N", "E", "S", "W"]


def is_direction(x: str) -> TypeIs[Direction]:
    return x in {"N", "E", "S", "W"}


def maybe_direction(x: str) -> None:
    if is_direction(x):
        print(f"{x} is a cardinal direction")
    else:
        print(f"{x} is not a cardinal direction")


maybe_direction("E")
maybe_direction("West")

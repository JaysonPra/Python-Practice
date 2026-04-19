from typing import Generic, TypeVarTuple, Unpack

Ts = TypeVarTuple("Ts")


class Tensor(Generic[Unpack[Ts]]):
    def __init__(self, shape: tuple[Unpack[Ts]]):
        self.shape = shape


vector = Tensor[int]((100,))
matrix = Tensor[int, int]((1080, 1920))

print(f"Vector dimensions: {len(vector.shape)}")
print(f"Matrix dimensions: {len(matrix.shape)}")

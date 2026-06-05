class CircularStreamer:
    def __init__(self, data: list[int], max_reads: int) -> None:
        self.data = data
        self.max_reads = max_reads
        self.total_reads: int = 0
        self.tracker: int = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.total_reads == self.max_reads:
            raise StopIteration

        current = self.data[self.tracker]
        self.tracker = (self.tracker + 1) % len(self.data)
        self.total_reads += 1

        return current


if __name__ == "__main__":
    abc = CircularStreamer([1, 2, 3, 4, 5], 8)

    for i in abc:
        print(i)

from typing import Any, Iterable, Iterator


def Zip(*iters: Iterable[Any]) -> Iterator[tuple[Any, ...]]:
    iterators = [iter(it) for it in iters]

    while True:
        try:
            items = []
            for it in iterators:
                items.append(next(it))
            yield tuple(items)

        except StopIteration:
            return


firstList = [1, 2, 3, 4, 5]
secondList = [6, 7, 8, 9, 10]

for first, second in Zip(firstList, secondList):
    print(first, second)

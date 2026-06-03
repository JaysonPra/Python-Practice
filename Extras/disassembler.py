import dis


def use_explicit_loop(n: int) -> list[int]:
    squared_list: list[int] = []
    for i in range(n):
        squared_list.append(i**2)

    return squared_list


def use_comprehension(n: int) -> list[int]:
    squared_list: list[int] = [x**2 for x in range(n)]

    return squared_list


if __name__ == "__main__":
    dis.dis(use_explicit_loop)
    print("-" * 20)
    dis.dis(use_comprehension)

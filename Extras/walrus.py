def main() -> None:
    print("Enter numbers (0 to stop):")

    inputs = []
    while (v := int(input("> "))) != 0:
        inputs.append(v)

    evens = [n for n in inputs if n % 2 == 0]
    unique_evens = sorted(set(evens))

    print(f"Unique evens: {unique_evens}")
    print(f"Number of unique evens: {len(unique_evens)}")


if __name__ == "__main__":
    main()

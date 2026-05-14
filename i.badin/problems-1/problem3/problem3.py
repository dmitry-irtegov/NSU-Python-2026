import sys
from collections.abc import Iterator


def collatz_sequence(n: int) -> Iterator[int]:
    if n <= 0:
        raise ValueError("n must be a positive integer")

    def generate() -> Iterator[int]:
        current: int = n

        while True:
            yield current

            if current == 1:
                return

            if current % 2 == 0:
                current //= 2
            else:
                current = 3 * current + 1

    return generate()


def main() -> None:
    raw_value: str = input().strip()

    if not raw_value:
        print("Input error: empty input", file=sys.stderr)
        return

    try:
        n: int = int(raw_value)
    except ValueError:
        print("Input error: expected integer", file=sys.stderr)
        return

    try:
        sequence: Iterator[int] = collatz_sequence(n)
    except ValueError as error:
        print(error, file=sys.stderr)
        return

    print(" -> ".join(str(value) for value in sequence))


if __name__ == "__main__":
    main()

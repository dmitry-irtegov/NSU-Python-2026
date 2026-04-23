#!/usr/bin/python
from collections.abc import Iterator
from sys import stderr, argv


def collatz(num: int) -> Iterator[int]:
    if num <= 0:
        raise ValueError("Number must be positive")
    while True:
        yield num
        if num == 1:
            break
        num = num // 2 if num % 2 == 0 else 3 * num + 1


def run_test() -> None:
    assert list(collatz(6)) == [6, 3, 10, 5, 16, 8, 4, 2, 1]

    assert list(collatz(1)) == [1]

    assert list(collatz(3)) == [3, 10, 5, 16, 8, 4, 2, 1]

    try:
        list(collatz(0))
        assert False
    except ValueError:
        pass

    try:
        list(collatz(-5))
        assert False
    except ValueError:
        pass

    print("ALL TESTS PASSED")


def main() -> None:
    while True:
        try:
            a = int(input())
            break
        except ValueError:
            print("Need number")
        except Exception as e:
            print(f"Unexpected error: {e}", file=stderr)
            raise

    res = collatz(a)
    print(" -> ".join(map(str, res)))


if __name__ == "__main__":
    if "test" in argv:
        run_test()
    else:
        main()

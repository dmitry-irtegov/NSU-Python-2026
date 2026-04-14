#!/usr/bin/env python3

from sys import stderr


def pythagorean_triples(num):
    if num <= 0:
        raise ValueError("number must be a non-negative integer")

    squares = {i * i: i for i in range(1, num + 1)}
    return [(x, y, squares[x * x + y * y])
            for x in range(1, num + 1)
            for y in range(x, num + 1)
            if x * x + y * y in squares]


if __name__ == "__main__":
    try:
        n = int(input("Enter number: "))
        print(pythagorean_triples(n))
    except KeyboardInterrupt:
        print("Shutting down...")
    except Exception as e:
        print(f"Exception in main(): {e}", file=stderr)

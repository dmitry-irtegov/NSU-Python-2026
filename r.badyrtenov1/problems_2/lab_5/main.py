#!/usr/bin/env python3

from functools import reduce
from sys import stderr


def primes(num):
    return [i for i, val in enumerate(
        reduce(
            lambda s, i: (
                s if not s[i] else
                s.__setitem__(slice(i * i, num + 1, i), [False] * len(range(i * i, num + 1, i))) or s
            ),
            range(2, int(num ** 0.5) + 1),
            [True] * (num + 1)
        )
    ) if val and i > 1]


if __name__ == "__main__":
    try:
        n = int(input("Enter number: "))
        print(primes(n))
    except KeyboardInterrupt:
        print("Shutting down...")
    except Exception as e:
        print(f"Exception in main(): {e}", file=stderr)

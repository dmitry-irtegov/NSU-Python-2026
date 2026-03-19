#!/usr/bin/python

from sys import stderr


def get_primes(N: int) -> list[list[int]]:
    if N <= 0:
        raise ValueError("Number must be positive")

    res = []
    i = 2

    while i * i <= N:
        if N % i == 0:
            count = 0
            while N % i == 0:
                N //= i
                count += 1
            res.append([i, count])
        i += 1

    if N > 1:
        res.append([N, 1])

    return res


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

    res = get_primes(a)
    print(res)


if __name__ == "__main__":
    main()

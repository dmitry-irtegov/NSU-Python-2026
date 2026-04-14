#!/usr/bin/env python3

from sys import stderr


def primes(num):
    if num <= 1:
        return []

    sieve = [True] * (num + 1)
    for i in range(2, int(num ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i: num + 1: i] = [False] * len(range(i * i, num + 1, i))

    return [i for i in range(2, num + 1) if sieve[i]]


if __name__ == "__main__":
    try:
        n = int(input("Enter number: "))
        print(primes(n))
    except KeyboardInterrupt:
        print("Shutting down...")
    except Exception as e:
        print(f"Exception in main(): {e}", file=stderr)

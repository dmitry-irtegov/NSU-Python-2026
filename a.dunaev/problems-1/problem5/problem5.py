#!/usr/bin/python

import math
import random


def _is_prime(n: int) -> bool:
    if n < 2:
        return False

    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    for prime in small_primes:
        if n == prime:
            return True
        if n % prime == 0:
            return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for base in small_primes:
        if base >= n:
            continue
        x = pow(base, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


def _pollard_rho(n: int) -> int:
    if n % 2 == 0:
        return 2

    rng = random.Random(n)

    while True:
        x = rng.randrange(2, n - 1)
        y = x
        c = rng.randrange(1, n - 1)
        d = 1

        while d == 1:
            x = (pow(x, 2, n) + c) % n
            y = (pow(y, 2, n) + c) % n
            y = (pow(y, 2, n) + c) % n
            d = math.gcd(abs(x - y), n)

        if d != n:
            return d


def _factorize(n: int, factors: list[int]) -> None:
    if n == 1:
        return
    if _is_prime(n):
        factors.append(n)
        return

    divisor = _pollard_rho(n)
    _factorize(divisor, factors)
    _factorize(n // divisor, factors)


def to_prime(n: int) -> list[list[int]]:
    if n < 1:
        return []

    factors: list[int] = []
    _factorize(n, factors)
    factors.sort()

    out: list[list[int]] = []
    for factor in factors:
        if out and out[-1][0] == factor:
            out[-1][1] += 1
        else:
            out.append([factor, 1])

    return out


if __name__ == "__main__":
    num = 12
    assert to_prime(num) == [[2, 2], [3, 1]]

    num = 60
    assert to_prime(num) == [[2, 2], [3, 1], [5, 1]]

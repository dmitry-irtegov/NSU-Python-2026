#!/usr/bin/python

from math import sqrt

def sieve(n:int) -> list[int]:
    if n <= 0:
        raise ValueError("Number must be positive")

    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for i in range(2, int(sqrt(n)) + 1):
        if prime[i]:
            for j in range(i*i, n + 1, i):
                prime[j] = False

    return [i for i in range(n + 1) if prime[i]]

def get_primes(N:int) -> list[list[int]]:
    if N <= 0:
        raise ValueError("Number must be positive")

    primes = sieve(N)
    res = []

    for a in primes:
        if (N/a).is_integer():
            b = 1
            while (N/a**(b+1)).is_integer():
                b += 1
            res.append([a, b])

    return res

from sys import stderr

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

def run_test() -> None:
    N = 180
    primes = get_primes(N)

    for a, b in primes:
        assert (N := N / a**b).is_integer()

    assert N == 1

    N = 6*7*8*9*11*13*15
    primes = get_primes(N)

    for a, b in primes:
        assert (N := N / a**b).is_integer()

    assert N == 1


    N = 461
    primes = get_primes(N)

    for a, b in primes:
        assert (N := N / a**b).is_integer()

    assert N == 1


    try:
        get_primes(0)
        assert False
    except ValueError:
        pass

    try:
        get_primes(-5)
        assert False
    except ValueError:
        pass
    print("All tests passed!")


from sys import argv

if __name__ == "__main__":
    if "test" in argv:
        run_test()
    else:
        main()
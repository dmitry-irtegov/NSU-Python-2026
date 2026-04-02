#!/usr/bin/env python3

from sys import stderr


def factorize(num):
    res = []
    div = 2
    exp = 0
    while num > 1:
        if num % div == 0:
            num //= div
            exp += 1
        else:
            if exp != 0:
                res.append([div, exp])
                exp = 0
            div += 1
    if exp != 0:
        res.append([div, exp])
    return res


if __name__ == "__main__":
    try:
        n = int(input("Enter number: "))
        print(factorize(n))
    except KeyboardInterrupt:
        print("Shutting down...")
    except Exception as e:
        print(f"Exception in main(): {e}", file=stderr)

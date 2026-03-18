#!/usr/bin/env python3

from sys import stderr


def collatz_sequence(num):
    print(num, end="")
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        print(f" -> {num}", end="")


if __name__ == "__main__":
    try:
        n = int(input("Enter number: "))
        collatz_sequence(n)
    except KeyboardInterrupt:
        print("Shutting down...")
    except Exception as e:
        print(f"Exception in main(): {e}", file=stderr)

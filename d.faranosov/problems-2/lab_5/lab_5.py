from sys import argv, stderr
from math import isqrt

def get_simple(n):
    if n <= 2:
        return []
    return [2] + [number for number in range(3, n, 2) if
            all(number % y != 0 for y in range(3, isqrt(number) + 1, 2))]

if __name__ == "__main__":
    if len(argv) < 2:
        print("Wrong argument count", file=stderr)
        exit(1)
    try:
        max_num = int(argv[1])
        print(get_simple(max_num))
    except ValueError:
        print("argument is not an int", file=stderr)
        exit(1)

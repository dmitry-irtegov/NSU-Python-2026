def collatz_sequence(n: int):
    if not isinstance(n, int):
        raise TypeError("n must be int")
    if n <= 0:
        raise ValueError("n must be > 0")

    seen = set()
    while n not in seen:
        yield n

        if n == 1:
            return

        seen.add(n)

        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1


def main():
    s = input().strip()
    n = int(s)
    print(" -> ".join(str(x) for x in collatz_sequence(n)))


if __name__ == "__main__":
    main()

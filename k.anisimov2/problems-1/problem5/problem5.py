import sys


def factorize(number):
    if number <= 1:
        print(
            f"Invalid number for factorization: {number}. Expected an integer > 1.",
            file=sys.stderr,
        )
        return []

    res = []
    p = 2
    while p * p <= number:
        if number % p == 0:
            k = 0
            while number % p == 0:
                number //= p
                k += 1
            res.append([p, k])
        p += 1 if p == 2 else 2

    if number > 1:
        res.append([number, 1])
    return res


def main():
    try:
        raw = input()
        number = int(raw)
    except KeyboardInterrupt:
        print("Interrupted by user.", file=sys.stderr)
        return
    except Exception as e:
        print(f"Input error: {e}", file=sys.stderr)
        return

    res = factorize(number)
    if not res:
        return

    print(res)


if __name__ == "__main__":
    main()
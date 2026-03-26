import sys


def generate_pythagorean_triples(n):
    if not isinstance(n, int):
        raise TypeError("number must be an integer")
    if n <= 0:
        raise ValueError("number must be a positive integer")

    return [
        (x, y, z)
        for z in range(1, n + 1)
        for y in range(1, z)
        for x in range(1, y + 1)
        if x * x + y * y == z * z
    ]


def main():
    try:
        s = input().strip()
        n = 10 if s == "" else int(s)
    except KeyboardInterrupt:
        print("Interrupted by user.", file=sys.stderr)
        return
    except Exception as e:
        print(f"Input error: {e}", file=sys.stderr)
        return

    try:
        triples = generate_pythagorean_triples(n)
    except Exception as e:
        print(f"Input error: {e}", file=sys.stderr)
        return

    for t in triples:
        print(t)


if __name__ == "__main__":
    main()
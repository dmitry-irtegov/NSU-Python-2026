import sys


def generate_pythagorean_triples(n: int):
    if not isinstance(n, int):
        print("Error: number must be an integer", file=sys.stderr)
        return []
    if n <= 0:
        print("Error: number must be a positive integer", file=sys.stderr)
        return []

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

    triples = generate_pythagorean_triples(n)
    if not triples:
        return

    for t in triples:
        print(t)


if __name__ == "__main__":
    main()
import sys


def generate_primes(n):
    if not isinstance(n, int):
        raise TypeError("number must be an integer")
    if n < 2:
        raise ValueError("number must be at least 2")

    return [
        x
        for x in range(2, n + 1)
        if all(x % d != 0 for d in range(2, int(x ** 0.5) + 1))
    ]


def format_primes(primes):
    if not isinstance(primes, list):
        raise TypeError("primes must be a list")
    return " ".join(str(x) for x in primes)


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
        primes = generate_primes(n)
        text = format_primes(primes)
    except Exception as e:
        print(f"Input error: {e}", file=sys.stderr)
        return

    if text != "":
        print(text)

if __name__ == "__main__":
    main()
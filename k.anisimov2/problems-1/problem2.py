import sys


def clamp_sequence(seq, a, b):
    if a > b:
        print(f"Invalid range: a={a} > b={b}.", file=sys.stderr)
        return []
    return [a if x < a else b if x > b else x for x in seq]


def main():
    try:
        raw_seq = input()
        raw_bounds = input()

        seq = [int(x) for x in raw_seq.split()]
        a_str, b_str = raw_bounds.split()
        a = int(a_str)
        b = int(b_str)
    except Exception as e:
        print(f"Input error: {e}", file=sys.stderr)
        return

    res = clamp_sequence(seq, a, b)
    if not res and seq and a > b:
        return

    print(res)


if __name__ == "__main__":
    main()
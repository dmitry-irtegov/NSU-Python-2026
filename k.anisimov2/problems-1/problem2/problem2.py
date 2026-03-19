import sys

def clamp_sequence(seq, a, b):
    if a > b:
        raise ValueError(f"Invalid range: a={a} > b={b}.")
    return [a if x < a else b if x > b else x for x in seq]


def main():
    try:
        raw_seq = input()
        raw_bounds = input()

        seq = [int(x) for x in raw_seq.split()] if raw_seq.strip() else []

        parts = raw_bounds.split()
        if len(parts) != 2:
            raise ValueError("Bounds must contain exactly two integers: a b")

        a = int(parts[0])
        b = int(parts[1])

        res = clamp_sequence(seq, a, b)
        print(res)

    except KeyboardInterrupt:
        print("Interrupted by user.", file=sys.stderr)
        return
    except Exception as e:
        print(f"Input error: {e}", file=sys.stderr)
        return


if __name__ == "__main__":
    main()
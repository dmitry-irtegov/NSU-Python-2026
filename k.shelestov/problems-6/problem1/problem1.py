import random
import re
import sys
import argparse


def process_word(word, mode, rng):
    if len(word) <= 2:
        return word

    middle = list(word[1:-1])

    if mode == "random":
        rng.shuffle(middle)
    else:
        middle.sort()

    return word[0] + "".join(middle) + word[-1]


def process_text(text, mode, rng):
    tokens = re.findall(r"\w+|[^\w]+", text)
    result = []

    for t in tokens:
        if t.isalpha():
            result.append(process_word(t, mode, rng))
        else:
            result.append(t)

    return "".join(result)


def main():
    parser = argparse.ArgumentParser(description="Shuffle or sort inner letters of words")

    parser.add_argument(
        "--mode",
        choices=["random", "sort"],
        default="random",
        help="Processing mode"
    )

    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for reproducibility"
    )

    args = parser.parse_args()

    rng = random.Random(args.seed)

    try:
        for line in sys.stdin:
            if line.strip():
                print(process_text(line.rstrip("\n"), args.mode, rng))

    except KeyboardInterrupt:
        print("\nInterrupted")
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        raise


if __name__ == "__main__":
    main()
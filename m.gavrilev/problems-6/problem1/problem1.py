#!/usr/bin/env python3

import sys
from itertools import groupby

RANDOM_MODE = "random"
SORT_MODE = "sort"
MODES = (RANDOM_MODE, SORT_MODE)


def random_middle(middle, rng):
    return "".join(rng.sample(middle, len(middle)))


def sort_middle(middle):
    return "".join(sorted(middle, key=str.casefold))


def transform_word(word, transform_middle):
    if len(word) <= 3:
        return word

    return word[0] + transform_middle(word[1:-1]) + word[-1]


def transform_text(text, transform_middle):
    result = []

    for is_word, chars in groupby(text, key=str.isalpha):
        part = "".join(chars)

        if is_word:
            result.append(transform_word(part, transform_middle))
        else:
            result.append(part)

    return "".join(result)


def main():
    import argparse
    import random
    from functools import partial

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=MODES,
        default=RANDOM_MODE,
        help="how to transform inner word letters",
    )
    parser.add_argument(
        "--seed",
        type=int,
        help="seed for repeatable random mode",
    )
    args = parser.parse_args()

    if args.mode == RANDOM_MODE:
        rng = random.Random(args.seed)
        transform_middle = partial(random_middle, rng=rng)
    else:
        transform_middle = sort_middle

    for line in sys.stdin:
        print(transform_text(line, transform_middle), end="")


if __name__ == "__main__":
    try:
        main()
    except EOFError as e:
        print(f"EOFError: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("KeyboardInterrupt: interrupted", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

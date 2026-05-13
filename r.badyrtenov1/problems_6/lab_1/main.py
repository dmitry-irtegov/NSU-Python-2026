#!/usr/bin/env python3

import random
from re import compile, UNICODE
from sys import stderr, stdin, argv

WORD_RE = compile(r"[^\W\d_]+", UNICODE)


def transform_word(word, mode):
    if len(word) <= 3:
        return word

    middle = list(word[1:-1])

    if mode == "sorted":
        middle.sort()
    elif mode == "random":
        random.shuffle(middle)
    else:
        raise ValueError("mode must be 'random' or 'sorted'")

    return word[0] + "".join(middle) + word[-1]


def transform_text(text, mode):
    return WORD_RE.sub(lambda m: transform_word(m.group(0), mode), text)


if __name__ == "__main__":
    try:
        print("\n" + transform_text(stdin.read(), "sorted" if (len(argv) >= 2 and argv[1] == "sorted") else "random"))
    except KeyboardInterrupt:
        print("Shutting down...", file=stderr)
    except Exception as e:
        print(f"Exception in main(): {e}", file=stderr)

import random
import re
import sys


def randomize_words(s: str, seed: int = 42, mode: str = "random"):
    if mode not in ("random", "sort"):
        raise ValueError(f"Invalid mode: {mode}")
    if mode == "random":
        random.seed(seed)

    tokens = re.findall(r"\w+|[^\w]+", s)
    result = []

    for token in tokens:
        if token.isalpha() and len(token) > 2:
            middle = list(token[1:-1])

            if mode == "random":
                random.shuffle(middle)
            elif mode == "sort":
                middle.sort()

            new_word = token[0] + "".join(middle) + token[-1]
            result.append(new_word)
        else:
            result.append(token)
    return "".join(result)


def main() -> None:
    mode: str
    if len(sys.argv) > 1 and sys.argv[1] == "sort":
        mode = "sort"
    else:
        mode = "random"

    while True:
        try:
            pattern = input("\n> ").strip()
        except EOFError:
            print("\nEOF exiting")
            break

        if pattern == "":
            continue

        res = randomize_words(pattern, 42, mode=mode)

        print(res)


if __name__ == "__main__":
    main()

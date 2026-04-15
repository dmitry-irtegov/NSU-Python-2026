import random
import re
import sys
from typing import List


def randomize_words(s: str, seed: int = 42, mode: str = "random") -> str:
    if mode not in ("random", "sort"):
        raise ValueError(f"Invalid mode: {mode}")

    if mode == "random":
        random.seed(seed)

    tokens: List[str] = re.findall(r"\w+|[^\w]+", s)
    result: List[str] = []

    for token in tokens:
        if token.isalpha() and len(token) > 2:
            middle: List[str] = list(token[1:-1])

            if mode == "random":
                random.shuffle(middle)
            else:
                middle.sort()

            new_word: str = token[0] + "".join(middle) + token[-1]
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

    for line in sys.stdin:
        line = line.rstrip("\n")

        if line == "":
            continue

        res = randomize_words(line, 42, mode=mode)
        print(res)


if __name__ == "__main__":
    main()

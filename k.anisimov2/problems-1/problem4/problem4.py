import sys


NUMBER_WORDS = (
    "no", "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine", "ten"
)

def number_to_words(n):
    if not isinstance(n, int):
        raise TypeError("n must be int")
    if n < 0 or n >= len(NUMBER_WORDS):
        raise ValueError("n must be in range 0..10")
    return NUMBER_WORDS[n]


def _bottles_word(n):
    if not isinstance(n, int):
        raise TypeError("n must be int")
    if n < 0:
        raise ValueError("n must be >= 0")
    return "bottle" if n == 1 else "bottles"


def generate_ten_green_bottles(start=10):
    if not isinstance(start, int):
        raise TypeError("start must be int")
    if start <= 0 or start > 10:
        raise ValueError("start must be in range 1..10")

    lines = []
    for n in range(start, 0, -1):
        next_n = n - 1

        cur_word_cap = number_to_words(n).capitalize()
        cur_bottle = _bottles_word(n)

        next_word = number_to_words(next_n)
        next_bottle = _bottles_word(next_n)

        lines.append(f"{cur_word_cap} green {cur_bottle} hanging on the wall,")
        lines.append(f"{cur_word_cap} green {cur_bottle} hanging on the wall,")

        if n == 1:
            lines.append("If that one green bottle should accidentally fall")
            lines.append("There’ll be no green bottles hanging on the wall.")
        else:
            lines.append("And if one green bottle should accidentally fall,")
            lines.append(f"There’ll be {next_word} green {next_bottle} hanging on the wall.")

    return "\n".join(lines) + "\n"


def main():
    try:
        raw = input().strip()
        start = 10 if raw == "" else int(raw)
    except KeyboardInterrupt:
        print("Interrupted by user.", file=sys.stderr)
        return
    except Exception as e:
        print(f"Input error: {e}", file=sys.stderr)
        return

    try:
        text = generate_ten_green_bottles(start)
    except Exception as e:
        print(f"Input error: {e}", file=sys.stderr)
        return

    print(text, end="")


if __name__ == "__main__":
    main()
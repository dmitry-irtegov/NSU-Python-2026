import sys


def number_to_words(n):
    words = ["no", "one", "two", "three", "four", "five",
             "six", "seven", "eight", "nine", "ten"]
    return words[n]


def _bottles_word(n):
    return "bottle" if n == 1 else "bottles"


def generate_ten_green_bottles(start=10):
    if not isinstance(start, int):
        print(f"Invalid start: {start}. Expected an integer.", file=sys.stderr)
        return ""
    if start <= 0 or start > 10:
        print(f"Invalid start: {start}. Expected an integer in [1, 10].", file=sys.stderr)
        return ""

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
        if raw == "":
            start = 10
        else:
            start = int(raw)
    except KeyboardInterrupt:
        print("Interrupted by user.", file=sys.stderr)
        return
    except Exception as e:
        print(f"Input error: {e}", file=sys.stderr)
        return

    text = generate_ten_green_bottles(start)
    if text == "":
        return

    print(text, end="")


if __name__ == "__main__":
    main()
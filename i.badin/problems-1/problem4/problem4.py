NUMBER_WORDS = [
    "no",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
]
WALL_SUFFIX = "hanging on the wall"
FALL_SUFFIX = "one green bottle should accidentally fall"
REGULAR_THIRD_LINE = f"And if {FALL_SUFFIX},"
LAST_THIRD_LINE = f"If that {FALL_SUFFIX}"


def bottles_phrase(count: int, capitalize: bool = False) -> str:
    word = NUMBER_WORDS[count]
    if capitalize:
        word = word.capitalize()
    bottle_word = "bottle" if count == 1 else "bottles"
    return f"{word} green {bottle_word}"


def build_verse(count: int) -> str:
    current_phrase = bottles_phrase(count, capitalize=True)
    next_phrase = bottles_phrase(count - 1)

    line1 = f"{current_phrase} {WALL_SUFFIX},"
    line2 = line1

    if count == 1:
        line3 = LAST_THIRD_LINE
    else:
        line3 = REGULAR_THIRD_LINE

    line4 = f"There'll be {next_phrase} {WALL_SUFFIX}."
    return "\n".join((line1, line2, line3, line4))


def generate_song() -> str:
    return "\n".join(build_verse(count) for count in range(10, 0, -1))


def main():
    print(generate_song())


if __name__ == "__main__":
    main()

def bottles_word(n: int) -> str:
    if not isinstance(n, int):
        raise TypeError("n must be int")
    if n < 0:
        raise ValueError("n must be >= 0")
    return "bottle" if n == 1 else "bottles"


def number_word(n: int) -> str:
    if not isinstance(n, int):
        raise TypeError("n must be int")

    words = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
    }

    if n not in words:
        raise ValueError("n must be in range 1..10")
    return words[n]


def print_song():
    for n in range(10, 0, -1):
        n_word = number_word(n)
        next_n_word = "no" if n == 1 else number_word(n - 1).lower()

        print(f"{n_word} green {bottles_word(n)} hanging on the wall,\n" * 2, end='')

        line_start = "If that" if n == 1 else "And if"
        comma = "" if n == 1 else ","
        print(f"{line_start} one green bottle should accidentally fall{comma}")

        print(f"There'll be {next_n_word} green {bottles_word(n - 1)} hanging on the wall.")


if __name__ == "__main__":
    print_song()
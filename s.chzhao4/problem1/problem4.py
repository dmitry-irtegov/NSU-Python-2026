def generate_ten_green_bottles() -> list:
    numbers = [
        "No", "One", "Two", "Three", "Four",
        "Five", "Six", "Seven", "Eight", "Nine", "Ten"
    ]

    lyrics = []

    for i in range(10, 0, -1):
        current_num_word = numbers[i]
        next_num_word = numbers[i - 1].lower()

        bottle_str = "bottle" if i == 1 else "bottles"
        next_bottle_str = "bottle" if (i - 1) == 1 else "bottles"

        line = f"{current_num_word} green {bottle_str} hanging on the wall,"

        lyrics.append(line)
        lyrics.append(line)

        if i == 1:
            lyrics.append("If that one green bottle should accidentally fall,")
        else:
            lyrics.append("And if one green bottle should accidentally fall,")

        lyrics.append(f"There'll be {next_num_word} green {next_bottle_str} hanging on the wall.")

    return lyrics


def sing_ten_green_bottles() -> None:
    lyrics_lines = generate_ten_green_bottles()
    for line in lyrics_lines:
        print(line)

if __name__ == "__main__":
    sing_ten_green_bottles()
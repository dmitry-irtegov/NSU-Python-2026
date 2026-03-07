def generate_bottles_song():
    numbers = [
        "Ten", "Nine", "Eight", "Seven", "Six",
        "Five", "Four", "Three", "Two", "One", "No"
    ]

    lines = []

    for i in range(10, 0, -1):
        current = numbers[10 - i]
        next_one = numbers[11 - i]

        bottle_word = "bottle" if i == 1 else "bottles"

        line = f"{current} green {bottle_word} hanging on the wall,"
        lines.append(line)
        lines.append(line)

        base_line = "one green bottle should accidentally fall,"
        if i == 1:
            start = "If that "
        else:
            start = "And if "
        lines.append(start + base_line)

        next_line = line.replace(current, next_one.lower()).replace(",", ".")
        lines.append("There'll be " + next_line)

    return "\n".join(lines)

def main():
    print(generate_bottles_song())

if __name__ == "__main__":
    main()
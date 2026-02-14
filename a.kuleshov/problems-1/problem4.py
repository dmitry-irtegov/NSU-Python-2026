numbers = [
    "Ten", "Nine", "Eight", "Seven", "Six",
    "Five", "Four", "Three", "Two", "One", "No"
]

for i in range(10, 0, -1):
    current = numbers[10 - i]
    next_one = numbers[11 - i]

    bottle_word = "bottle" if i == 1 else "bottles"

    line = f"{current} green {bottle_word} hanging on the wall,"
    print(line)
    print(line)

    base_line = "one green bottle should accidentally fall,"
    if i == 1:
        start = "If that "
    else:
        start = "And if "
    print(start + base_line)

    next_line = line.replace(current, next_one.lower()).replace(",", ".")
    print("There'll be " + next_line)

NUMBERS = ["no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

FIRST_LINE_TEMPLATE = "{} green bottle{} hanging on the wall,"
THIRD_LINE_TEMPLATE = "{} one green bottle should accidentally fall,"
FOURTH_LINE_TEMPLATE = "There'll be {} green bottles hanging on the wall."

BOTTLES_NUMBER = 10
while BOTTLES_NUMBER > 0:
    first_line = FIRST_LINE_TEMPLATE.format(
        NUMBERS[BOTTLES_NUMBER].capitalize(),
        "s" if BOTTLES_NUMBER > 1 else ""
    )
    print(first_line)
    print(first_line)

    third_line = THIRD_LINE_TEMPLATE.format(
        "And if" if BOTTLES_NUMBER > 1 else "If that"
    )
    print(third_line)

    BOTTLES_NUMBER -= 1

    fourth_line = FOURTH_LINE_TEMPLATE.format(
        NUMBERS[BOTTLES_NUMBER]
    )
    print(fourth_line)


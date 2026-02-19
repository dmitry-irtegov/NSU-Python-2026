def print_ten_green_bottles():
    parts = []
    numToWordUppercase = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
                          6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"}

    numToWordLastLine = {0: "no", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
                         6: "six", 7: "seven", 8: "eight", 9: "nine"}

    for i in range(10, 0, -1):
        parts.append(f"{numToWordUppercase[i]} green bottles hanging on the wall,\n")
        parts.append(f"{numToWordUppercase[i]} green bottles hanging on the wall,\n")

        if i == 1:
            parts.append("If that ")
        else:
            parts.append("And if ")

        parts.append("one green bottle should accidentally fall\n")
        parts.append(f"There’ll be {numToWordLastLine[i - 1]} green bottles hanging on the wall.\n")

    print(''.join(parts))

if __name__ == '__main__':
    print_ten_green_bottles()
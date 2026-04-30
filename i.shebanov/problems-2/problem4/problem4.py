from sys import stderr, argv

def find_search(text: str, pattern: str) -> list[int]:
    indexes = []
    start = 0
    while 1:
        cur_index = text.find(pattern, start)
        if cur_index == -1:
            break
        indexes.append(cur_index)
        start = cur_index + 1
    return indexes


def result_line(found_indexes: list[int])->str:
    length = len(found_indexes)
    found_indexes = found_indexes if length < 5 else found_indexes[:5]
    result = f"Found {length} results."

    if length == 0:
        return result

    result += (
        "\nPositions: "
        + " ".join([str(index) for index in found_indexes])
        + ("..." if length > 5 else "")
    )
    return result

def main(pattern: str):
    try:
        with open("pi.txt", "r", encoding="utf-8") as file:
            file.read(2)
            text = file.read()
            text = text.replace("\n", "")

            indexes = find_search(text, pattern)

            print(result_line(indexes))
    except OSError as err:
        print("Cannot open file ", err, file=stderr)


if __name__ == "__main__":
    if len(argv) == 1:
        print("Usage: python3 problem4.py <pattern>", file=stderr)
        exit(1)
    if len(argv) == 2:
        main(argv[1])

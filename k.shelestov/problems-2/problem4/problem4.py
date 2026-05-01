import sys


def find_positions(data, pattern):
    positions = []
    start = 0

    while True:
        idx = data.find(pattern, start)
        if idx == -1:
            break
        positions.append(idx)
        start = idx + 1

    return positions


def main():
    try:
        with open("pi.txt", "r", encoding="utf-8") as file:
            file.read(2)
            text = file.read()
            text = text.replace("\n", "")

        seq = input("Enter sequence to search for:\n> ").strip()

        positions = find_positions(text, seq)

        print(f"Found {len(positions)} results.")
        if positions:
            print("Positions:", *positions[:5], "...")

    except OSError as err:
        print("Cannot open file", err, file=sys.stderr)


if __name__ == "__main__":
    main()
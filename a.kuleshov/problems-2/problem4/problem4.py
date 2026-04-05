def find_sequence_positions(pi_digits: str, sequence: str):
    positions = []
    index = pi_digits.find(sequence)

    while index != -1:
        positions.append(index)
        index = pi_digits.find(sequence, index + 1)

    return positions


def main():
    with open("pi.txt", "r", encoding="utf-8") as f:
        pi_digits = f.read()
    pi_digits = pi_digits.replace("\n", "")
    pi_digits = pi_digits.replace("3.", "")

    print("Enter sequence to search for.")
    sequence = input().strip()

    positions = find_sequence_positions(pi_digits, sequence)

    print(f"Found {len(positions)} results.")

    if positions:
        first_positions = positions[:5]

        if len(positions) > 5:
            print("Positions:", " ".join(map(str, first_positions)), "...")
        else:
            print("Positions:", " ".join(map(str, first_positions)))


if __name__ == "__main__":
    main()
def find_all(text, sub):
    start = 0
    positions = []
    while True:
        pos = text.find(sub, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    return positions

if __name__ == "__main__":
    path = input("Please enter pi file path: ")

    pi_str = ""
    try:
        with open(path) as f:
            pi_str = f.read()
    except Exception as e:
        print("error occurred during opening file: " + str(e))
        exit(1)

    pi_str = ''.join(filter(str.isdigit, pi_str[2:]))

    print("Enter sequence to search for")
    sequence = input("> ")

    positions = find_all(pi_str, sequence)

    print(f"Found {len(positions)} positions")
    if len(positions) > 5:
        print("Positions:", positions[:5], "...")
    else:
        print("Positions:", positions)


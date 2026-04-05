import sys


def load_pi_digits(filename):
    if not isinstance(filename, str):
        raise TypeError("filename must be a string")
    if filename == "":
        raise ValueError("filename must not be empty")

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    digits = content.replace(".", "").replace("\n", "").replace("\r", "")
    if digits == "" or not digits.isdigit():
        raise ValueError("file does not contain digits")

    return digits


def find_all_occurrences(text, pattern):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(pattern, str):
        raise TypeError("pattern must be a string")
    if pattern == "":
        raise ValueError("pattern must not be empty")
    if not pattern.isdigit():
        raise ValueError("pattern must contain only digits")

    positions = []
    start = 0

    while True:
        pos = text.find(pattern, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1

    return positions


def format_search_result(positions):
    if not isinstance(positions, list):
        raise TypeError("positions must be a list")

    count = len(positions)
    lines = [f"Found {count} results."]

    if count == 0:
        lines.append("Positions:")
    else:
        first_five = positions[:5]
        suffix = " ..." if count > 5 else ""
        lines.append("Positions: " + " ".join(str(x) for x in first_five) + suffix)

    return "\n".join(lines)


def main():
    try:
        pi_digits = load_pi_digits("pi.txt")
    except KeyboardInterrupt:
        print("Interrupted by user.", file=sys.stderr)
        return
    except Exception as e:
        print(f"File error: {e}", file=sys.stderr)
        return

    print("Enter sequence to search for.")
    try:
        pattern = input().strip()
    except KeyboardInterrupt:
        print("Interrupted by user.", file=sys.stderr)
        return
    except Exception as e:
        print(f"Input error: {e}", file=sys.stderr)
        return

    try:
        positions = find_all_occurrences(pi_digits, pattern)
        print(format_search_result(positions))
    except Exception as e:
        print(f"Input error: {e}", file=sys.stderr)
        return


if __name__ == "__main__":
    main()
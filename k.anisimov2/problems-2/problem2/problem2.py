import sys


def convert_dictionary(lines):
    if not isinstance(lines, list):
        raise TypeError("lines must be a list")

    latin_to_english = {}

    for line in lines:
        if not isinstance(line, str):
            raise TypeError("each line must be a string")

        parts = line.split(" - ")
        if len(parts) != 2:
            raise ValueError(f"invalid dictionary line: {line}")

        english = parts[0].strip()
        latin_words = [word.strip() for word in parts[1].split(",")]

        if not english:
            raise ValueError(f"empty english word in line: {line}")

        for latin in latin_words:
            if not latin:
                raise ValueError(f"empty latin word in line: {line}")
            if latin not in latin_to_english:
                latin_to_english[latin] = []
            latin_to_english[latin].append(english)

    result = []
    for latin in sorted(latin_to_english):
        english_words = sorted(latin_to_english[latin])
        result.append(f"{latin} - {', '.join(english_words)}")

    return result


def main():
    try:
        n = int(input().strip())
        lines = [input().strip() for _ in range(n)]
    except KeyboardInterrupt:
        print("Interrupted by user.", file=sys.stderr)
        return
    except Exception as e:
        print(f"Input error: {e}", file=sys.stderr)
        return

    try:
        result = convert_dictionary(lines)
    except Exception as e:
        print(f"Input error: {e}", file=sys.stderr)
        return

    for line in result:
        print(line)


if __name__ == "__main__":
    main()
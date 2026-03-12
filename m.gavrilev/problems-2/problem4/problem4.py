#!/usr/bin/env python3

import sys


def find_pattern(text, pattern):
    if not pattern or not pattern.isdigit():
        raise ValueError("Pattern must be a non-empty digit string")
    if not text or not text.isdigit():
        raise ValueError("Text must be a non-empty digit string")

    start = 0
    while True:
        pos = text.find(pattern, start)
        if pos == -1:
            break
        yield pos
        start = pos + 1


def format_positions(positions, count):
    if not positions:
        return "Positions: not found"

    parts = " ".join(map(str, positions))
    if count > len(positions):
        parts += " ..."

    return f"Positions: {parts}"


def search_and_print(text, pattern):
    try:
        count = 0
        first_five = []
        for pos in find_pattern(text, pattern):
            if count < 5:
                first_five.append(pos)
            count += 1
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return

    print(f"Found {count} results.")
    print(f"{format_positions(first_five, count)}")


def main():
    import os

    script_dir = os.path.dirname(os.path.abspath(__file__))
    pi_path = os.path.join(script_dir, "pi.txt")

    try:
        with open(pi_path) as f:
            text = f.read().replace("\n", "").replace("3.", "", 1)
    except FileNotFoundError:
        print(f"Error: {pi_path} not found", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Error: no permission to read {pi_path}", file=sys.stderr)
        sys.exit(1)
    except MemoryError:
        print(f"Error: {pi_path} is too large to read into memory", file=sys.stderr)
        sys.exit(1)
    except OSError as e:
        print(f"Error reading {pi_path}: {e}", file=sys.stderr)
        sys.exit(1)

    interactive = sys.stdin.isatty()
    prompt = "> " if interactive else ""

    while True:
        try:
            if interactive:
                print("\nEnter sequence to search for.")
            pattern = input(prompt)
        except EOFError:
            if interactive:
                print("\nEOF received", file=sys.stderr)
            break
        except KeyboardInterrupt:
            if interactive:
                print("\nInterrupted", file=sys.stderr)
            break
        search_and_print(text, pattern)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

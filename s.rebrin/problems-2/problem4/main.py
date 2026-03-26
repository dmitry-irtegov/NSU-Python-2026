from typing import Tuple, List
from re import sub
from sys import stderr


def find_in_pi_stream_regex(
    filename: str, pattern: str, chunk_size: int = 1024 * 1024
) -> Tuple[int, List[int]]:
    if not pattern:
        raise ValueError("Pattern must not be empty")

    tail: str = ""
    total: int = 0
    positions: List[int] = []

    global_pos: int = 0

    with open(filename, "r") as f:
        first_two = f.read(2)
        if first_two != "3.":
            tail = first_two
        else:
            global_pos = 0

        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break

            filtered: str = sub(r"\D", "", chunk)

            data: str = tail + filtered

            start: int = 0
            while True:
                idx: int = data.find(pattern, start)
                if idx == -1:
                    break

                real_pos: int = global_pos - len(tail) + idx
                total += 1

                if len(positions) < 5:
                    positions.append(real_pos)

                start = idx + 1

            if len(pattern) > 1:
                tail = data[-(len(pattern) - 1) :]
            else:
                tail = ""

            global_pos += len(filtered)

    return total, positions


def main() -> None:
    try:
        filename = "pi.txt"

        while True:
            pattern = input("\n> ").strip()

            if pattern == "":
                print("Pattern must not be empty")
                continue

            if not pattern.isdigit():
                print("Pattern must contain only digits")
                continue

            total, positions = find_in_pi_stream_regex(filename, pattern)

            print(f"Found {total} results.")
            if total > 0:
                print("Positions:", *positions, "...")
    except KeyboardInterrupt:
        print("Done")
        return
    except Exception as e:
        print(f"Unexpected error: {e}", file=stderr)
        raise


if __name__ == "__main__":
    main()

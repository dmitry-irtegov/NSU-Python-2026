from time import time
from typing import Tuple, List
from re import sub


def find_in_pi_stream(
    filename: str, pattern: str, chunk_size: int = 1024 * 1024
) -> Tuple[int, List[int], float]:
    if not pattern:
        raise ValueError("Pattern must not be empty")

    tail: str = ""
    total: int = 0
    positions: List[int] = []

    global_pos: int = 0

    glob_time = 0.0

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

            start_t = time()
            filtered: str = "".join(c for c in chunk if c.isdigit())
            end = time()

            glob_time += end - start_t

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

    return total, positions, glob_time


def find_in_pi_stream_regex(
    filename: str, pattern: str, chunk_size: int = 1024 * 1024
) -> Tuple[int, List[int], float]:
    if not pattern:
        raise ValueError("Pattern must not be empty")

    tail: str = ""
    total: int = 0
    positions: List[int] = []

    global_pos: int = 0

    glob_time = 0.0

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

            start_t = time()
            filtered: str = sub(r"\D", "", chunk)
            end = time()

            glob_time += end - start_t

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

    return total, positions, glob_time


def time_test() -> None:
    filename = "pi.txt"

    while True:
        try:
            pattern = input("\n> ").strip()
        except EOFError:
            print("\nEOF exiting")
            break

        if pattern == "":
            print("Pattern must not be empty")
            continue

        if not pattern.isdigit():
            print("Pattern must contain only digits")
            continue

        _, _, timee = find_in_pi_stream(filename, pattern)
        print("Time:", timee, "seconds")

        total, positions, timee = find_in_pi_stream_regex(filename, pattern)

        print("Time with regex:", timee, "seconds")

        print(f"Found {total} results.")
        if total > 0:
            print("Positions:", *positions, "...")


if __name__ == "__main__":
    time_test()

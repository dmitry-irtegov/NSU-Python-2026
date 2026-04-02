from time import time
from typing import Tuple, List
from re import sub


def find_in_pi_stream(
    filename: str, pattern: str, chunk_size: int = 1024 * 1024
) -> Tuple[int, List[int], float, float, float, float]:
    if not pattern:
        raise ValueError("Pattern must not be empty")

    tail: str = ""
    total: int = 0
    positions: List[int] = []

    global_pos: int = 0

    glob_time = 0.0
    glob_time1 = 0.0
    glob_time2 = 0.0
    glob_time3 = time()

    with open(filename, "r") as f:
        endd = time()
        glob_time3 = endd - glob_time3
        first_two = f.read(2)
        if first_two != "3.":
            tail = first_two
        else:
            global_pos = 0

        while True:
            start_t = time()
            chunk = f.read(chunk_size)

            end = time()

            glob_time1 += end - start_t
            if not chunk:
                break

            start_t = time()
            filtered: str = "".join(c for c in chunk if c.isdigit())

            end = time()

            glob_time2 += end - start_t

            data: str = tail + filtered

            start: int = 0

            start_t = time()
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

            end = time()

            glob_time += end - start_t

    return total, positions, glob_time, glob_time1, glob_time2, glob_time3


def find_in_pi_stream_regex(
    filename: str, pattern: str, chunk_size: int = 1024 * 1024
) -> Tuple[int, List[int], float, float, float, float]:
    if not pattern:
        raise ValueError("Pattern must not be empty")

    tail: str = ""
    total: int = 0
    positions: List[int] = []

    global_pos: int = 0

    glob_time3 = time()

    with open(filename, "r") as f:
        endd = time()
        glob_time3 = endd - glob_time3
        first_two = f.read(2)
        if first_two != "3.":
            tail = first_two
        else:
            global_pos = 0

        glob_time = 0.0
        glob_time1 = 0.0
        glob_time2 = 0.0

        while True:
            start_t = time()
            chunk = f.read(chunk_size)

            end = time()

            glob_time1 += end - start_t
            if not chunk:
                break

            glob_time2 += end - start_t
            filtered: str = sub(r"\D", "", chunk)
            end = time()

            glob_time2 += end - start_t

            data: str = tail + filtered

            start: int = 0

            start_t = time()
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

            end = time()

            glob_time += end - start_t

            global_pos += len(filtered)

    return total, positions, glob_time, glob_time1, glob_time2, glob_time3


def tst():
    filename = "pi.txt"
    start1 = time()
    _, _, t01, t11, t21, t31 = find_in_pi_stream(filename, "12345")
    end1 = time()

    print(
        "Time:",
        end1 - start1,
        "seconds\t",
        "Find:",
        t01,
        "Read:",
        t11,
        "Replace:",
        t21,
        "Open",
        t31,
    )
    print("Diff:", end1 - start1 - t01 - t11 - t21 - t31)

    start = time()
    _, _, t, t1, t2, t3 = find_in_pi_stream(filename, "43243")
    end = time()

    print(
        "Time:",
        end - start,
        "seconds\t",
        "Find:",
        t,
        "Read:",
        t1,
        "Replace:",
        t2,
        "Open",
        t3,
    )
    print("Diff:", end - start - t - t1 - t2 - t3)

    print("Find:", t - t01)
    print("Read:", t1 - t21)
    print("Replace:", t2 - t21)
    print("Opne:", t3 - t31)


if __name__ == "__main__":
    tst()

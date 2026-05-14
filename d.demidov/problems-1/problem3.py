import sys
import unittest
from collections.abc import Generator
from logging import root as logger


def collatz_conjecture_compute(num: int) -> Generator[int, None, None]:
    current_num: int = num
    if current_num < 1:
        raise ValueError("Number must be positive")

    while True:
        yield current_num
        if current_num == 1:
            break
        current_num = current_num // 2 if current_num % 2 == 0 else current_num * 3 + 1


def collatz_chain_to_string(num: int) -> str:
    chain: str = " -> ".join(str(value) for value in collatz_conjecture_compute(num))
    return chain


class TestCollatzConjectureCompute(unittest.TestCase):
    def test_collatz_conjecture_compute(self) -> None:
        res: list[int] = list(collatz_conjecture_compute(3))
        expected: list[int] = [3, 10, 5, 16, 8, 4, 2, 1]
        self.assertEqual(res, expected)

    def test_collatz_for_one(self) -> None:
        res: list[int] = list(collatz_conjecture_compute(1))
        expected: list[int] = [1]
        self.assertEqual(res, expected)

    def test_collatz_chain_to_string(self) -> None:
        res: str = collatz_chain_to_string(3)
        expected: str = "3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1"
        self.assertEqual(res, expected)

    def test_invalid_input(self) -> None:
        with self.assertRaises(ValueError):
            list(collatz_conjecture_compute(0))


def run_collatz_from_cli() -> None:
    try:
        input_num: int = 3 if len(sys.argv) < 2 else int(sys.argv[1])

        first: bool = True
        part: int
        for part in collatz_conjecture_compute(input_num):
            if not first:
                print(" -> ", end="")
            print(part, end="")
            first = False
    except Exception as err:
        logger.exception(f"Exception in collatz test: {err}")


if __name__ == "__main__":
    unittest.main()

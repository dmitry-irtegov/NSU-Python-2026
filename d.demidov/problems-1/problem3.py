import sys
import unittest
from logging import root as logger


def collatz_conjecture_compute(num: int) -> str:
    numbers_chain = []

    while num != 1:
        numbers_chain.append(str(num))
        num = num // 2 if num % 2 == 0 else num * 3 + 1

    numbers_chain.append("1")
    return " -> ".join(numbers_chain)


class TestCollatzConjectureCompute(unittest.TestCase):
    def test_collatz_conjecture_compute(self) -> None:
        result = collatz_conjecture_compute(3)
        self.assertEqual(result, "3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1")

    def test_collatz_for_one(self) -> None:
        result = collatz_conjecture_compute(1)
        self.assertEqual(result, "1")


def run_collatz_from_cli() -> None:
    try:
        input_num = 3 if len(sys.argv) < 2 else int(sys.argv[1])
        print(collatz_conjecture_compute(input_num))
    except Exception as err:
        logger.exception(f"Exception in collatz test: {err}")


if __name__ == "__main__":
    run_collatz_from_cli()

import sys
from logging import root as logger


def collatz_conjecture_compute(num: int) -> str:
    numbers_chain = []

    while num != 1:
        numbers_chain.append(str(num))
        num = num // 2 if num % 2 == 0 else num * 3 + 1

    numbers_chain.append("1")
    return " -> ".join(numbers_chain)


def test_collatz_conjecture_compute() -> None:
    try:
        input_num = 3 if len(sys.argv) < 2 else int(sys.argv[1])
        res = collatz_conjecture_compute(input_num)
        assert res.endswith(" -> 1")
        print(res)
    except Exception as err:
        logger.exception(f"Exception in collatz test: {err}")


if __name__ == "__main__":
    test_collatz_conjecture_compute()

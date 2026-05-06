import unittest


def prime_divisors(n: int) -> list[list[int]]:
    current_num: int = n
    result: list[list[int]] = []
    i: int = 2

    while i * i <= current_num:
        if current_num % i == 0:
            count: int = 0
            while current_num % i == 0:
                count += 1
                current_num //= i
            result.append([i, count])
        i += 1

    if current_num != 1:
        result.append([current_num, 1])
    return result


class TestPrimeDivisors(unittest.TestCase):
    def test_12(self) -> None:
        result: list[list[int]] = prime_divisors(12)
        expected: list[list[int]] = [[2, 2], [3, 1]]
        self.assertEqual(result, expected)

    def test_prime_number(self) -> None:
        result: list[list[int]] = prime_divisors(13)
        expected: list[list[int]] = [[13, 1]]
        self.assertEqual(result, expected)

    def test_power_of_prime(self) -> None:
        result: list[list[int]] = prime_divisors(64)
        expected: list[list[int]] = [[2, 6]]
        self.assertEqual(result, expected)

    def test_one(self) -> None:
        result: list[list[int]] = prime_divisors(1)
        expected: list[list[int]] = []
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

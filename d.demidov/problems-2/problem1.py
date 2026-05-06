import unittest
from math import gcd, sqrt


def gen_triplets(n: int) -> list[tuple[int, int, int]]:
    triplets: list[tuple[int, int, int]] = [
        (x, y, z)
        for x in range(1, n + 1)
        for y in range(x, n + 1)
        for z in [int(sqrt(x ** 2 + y ** 2))]
        if gcd(x, y) == 1 and z <= n and z ** 2 == x ** 2 + y ** 2
    ]
    return triplets


class TestGenTriplets(unittest.TestCase):
    def test_10(self) -> None:
        result: list[tuple[int, int, int]] = gen_triplets(10)
        expected: list[tuple[int, int, int]] = [(3, 4, 5)]
        self.assertEqual(result, expected)

    def test_30(self) -> None:
        result: list[tuple[int, int, int]] = gen_triplets(30)
        expected: list[tuple[int, int, int]] = [(3, 4, 5), (5, 12, 13), (7, 24, 25), (8, 15, 17), (20, 21, 29)]
        self.assertEqual(result, expected)

    def test_negative(self) -> None:
        self.assertEqual(gen_triplets(-1), [])

    def test_gcd(self) -> None:
        triplets: list[tuple[int, int, int]] = gen_triplets(50)
        x: int
        y: int
        for x, y, _ in triplets:
            self.assertEqual(gcd(x, y), 1)


if __name__ == "__main__":
    unittest.main()

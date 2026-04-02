import unittest
import math


def pythagorean_triples(n: int) -> list[tuple[int, int, int]]:
    return [
        (x, y, z)
        for x in range(1, n + 1)
        for y in range(x, n + 1)
        for z in [math.isqrt(x * x + y * y)]
        if z <= n and z * z == x * x + y * y
    ]


class TestPythagoreanTriples(unittest.TestCase):
    def test_example(self) -> None:
        self.assertEqual(
            pythagorean_triples(10),
            [(3, 4, 5), (6, 8, 10)]
        )

    def test_small(self) -> None:
        self.assertEqual(pythagorean_triples(4), [])

    def test_negative(self) -> None:
        self.assertEqual(pythagorean_triples(-10), [])

    def test_single_triple(self) -> None:
        self.assertEqual(pythagorean_triples(5), [(3, 4, 5)])

    def test_zero(self) -> None:
        self.assertEqual(pythagorean_triples(0), [])

    def test_large(self) -> None:
        n = 1000
        triples = pythagorean_triples(n)

        self.assertEqual(len(triples), 881)
        self.assertEqual(len(triples), len(set(triples)))
        self.assertEqual(triples, sorted(triples))

        for x, y, z in triples:
            self.assertTrue(1 <= x <= y <= z <= n)
            self.assertEqual(x * x + y * y, z * z)


if __name__ == "__main__":
    unittest.main()
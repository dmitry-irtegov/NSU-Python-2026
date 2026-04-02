import unittest
from math import gcd
from solution import primitive_pythagorean_triples


class TestPrimitivePythagoreanTriples(unittest.TestCase):

    def test_limit_5(self):
        self.assertEqual(
            primitive_pythagorean_triples(5),
            [(3, 4, 5)]
        )

    def test_limit_10(self):
        self.assertEqual(
            primitive_pythagorean_triples(10),
            [(3, 4, 5)]
        )

    def test_limit_20(self):
        self.assertEqual(
            primitive_pythagorean_triples(20),
            [(3, 4, 5), (5, 12, 13), (8, 15, 17)]
        )

    def test_limit_30(self):
        self.assertEqual(
            set(primitive_pythagorean_triples(30)),
            {
                (3, 4, 5),
                (5, 12, 13),
                (8, 15, 17),
                (7, 24, 25),
                (20, 21, 29)
            }
        )

    def test_equation(self):
        triples = primitive_pythagorean_triples(100)
        for x, y, z in triples:
            self.assertEqual(x*x + y*y, z*z)

    def test_primitive(self):
        triples = primitive_pythagorean_triples(100)
        for x, y, z in triples:
            self.assertEqual(gcd(gcd(x, y), z), 1)

    def test_limit(self):
        limit = 100
        triples = primitive_pythagorean_triples(limit)
        for x, y, z in triples:
            self.assertTrue(z <= limit)

    def test_sorted_inside(self):
        triples = primitive_pythagorean_triples(100)
        for x, y, z in triples:
            self.assertTrue(x <= y <= z)

    def test_no_scaled(self):
        triples = primitive_pythagorean_triples(100)
        self.assertNotIn((6, 8, 10), triples)
        self.assertNotIn((9, 12, 15), triples)

    def test_empty(self):
        self.assertEqual(
            primitive_pythagorean_triples(4),
            []
        )


if __name__ == "__main__":
    unittest.main()
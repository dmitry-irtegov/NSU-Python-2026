import unittest
from problem1 import pythagorean_triples

class TestPythagoreanTriplesInvalidInput(unittest.TestCase):
    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            pythagorean_triples(-5)

    def test_zero_raises(self):
        with self.assertRaises(ValueError) as ctx:
            pythagorean_triples(0)
        self.assertEqual(str(ctx.exception), "limit must be greater than 0")

class TestPythagoreanTriplesCorrectness(unittest.TestCase):
    def test_all_satisfy_pythagorean_theorem(self):
        for a, b, c in pythagorean_triples(1000):
            self.assertEqual(a * a + b * b, c * c)

    def test_all_sorted_a_le_b_le_c(self):
        for a, b, c in pythagorean_triples(1000):
            self.assertLessEqual(a, b)
            self.assertLessEqual(b, c)

    def test_all_within_limit(self):
        limit = 500
        for a, b, c in pythagorean_triples(limit):
            self.assertLessEqual(c, limit)

    def test_all_positive(self):
        for a, b, c in pythagorean_triples(100):
            self.assertGreater(a, 0)
            self.assertGreater(b, 0)
            self.assertGreater(c, 0)


class TestPythagoreanTriplesKnownValues(unittest.TestCase):
    def test_smallest_triple(self):
        triples = pythagorean_triples(5)
        self.assertIn((3, 4, 5), triples)

    def test_limit_4_returns_empty(self):
        self.assertEqual(pythagorean_triples(4), [])

    def test_limit_5_returns_one(self):
        triples = pythagorean_triples(5)
        self.assertEqual(len(triples), 1)

    def test_limit_13_contains_5_12_13(self):
        self.assertIn((5, 12, 13), pythagorean_triples(13))

    def test_limit_13_contains_primitive_and_multiple(self):
        triples = pythagorean_triples(13)
        self.assertIn((3, 4, 5), triples)    # примитивная
        self.assertIn((6, 8, 10), triples)   # кратная: 2*(3,4,5)
        self.assertIn((5, 12, 13), triples)  # примитивная

    def test_no_duplicates(self):
        triples = pythagorean_triples(200)
        self.assertEqual(len(triples), len(set(triples)))

if __name__ == '__main__':
    unittest.main()

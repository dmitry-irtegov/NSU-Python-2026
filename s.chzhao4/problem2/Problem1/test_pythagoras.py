import unittest
from problem1 import generate_pythagorean_triples

class TestPythagoreanTriples(unittest.TestCase):

    def test_no_triples_possible(self):
        self.assertEqual(generate_pythagorean_triples(4), [])
        self.assertEqual(generate_pythagorean_triples(0), [])
        self.assertEqual(generate_pythagorean_triples(-5), [])

    def test_minimum_triple(self):
        expected = [(3, 4, 5)]
        self.assertEqual(generate_pythagorean_triples(5), expected)

    def test_larger_range(self):
        expected = [
            (3, 4, 5),
            (5, 12, 13),
            (6, 8, 10),
            (9, 12, 15)
        ]
        self.assertEqual(generate_pythagorean_triples(15), expected)

    def test_no_duplicates(self):
        result = generate_pythagorean_triples(5)
        self.assertNotIn((4, 3, 5), result)
        self.assertEqual(len(result), 1)

if __name__ == '__main__':
    unittest.main()
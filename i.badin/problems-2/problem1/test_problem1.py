import unittest

from problem1 import pythagorean_triples


class TestPythagoreanTriples(unittest.TestCase):
    def test_negative_numbers_return_empty_list(self):
        for n in (-1, -10, -1000):
            self.assertEqual(pythagorean_triples(n), [])

    def test_zero_returns_empty_list(self):
        self.assertEqual(pythagorean_triples(0), [])

    def test_pythagorean_triples_for_5(self):
        self.assertEqual(pythagorean_triples(5), [(3, 4, 5)])

    def test_pythagorean_triples_for_13(self):
        self.assertEqual(pythagorean_triples(13), [(3, 4, 5), (5, 12, 13), (6, 8, 10)])

    def test_pythagorean_triples_for_300(self):
        triples = pythagorean_triples(300)

        self.assertIn((3, 4, 5), triples)
        self.assertIn((20, 21, 29), triples)
        self.assertIn((65, 72, 97), triples)
        self.assertIn((180, 240, 300), triples)
        self.assertTrue(all(z <= 300 for _, _, z in triples))
        self.assertEqual(len(triples), len(set(triples)))
        self.assertEqual(len(triples), 209)


if __name__ == "__main__":
    unittest.main()

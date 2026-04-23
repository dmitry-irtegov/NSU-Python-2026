import unittest
import problem1

class PythagoreanTriplesTests(unittest.TestCase):
    def test_returns_empty_list_for_small_n(self):
        self.assertEqual(problem1.pythagorean_triples(4), [])

    def test_returns_single_triple_for_five(self):
        self.assertEqual(problem1.pythagorean_triples(5), [(3, 4, 5)])

    def test_returns_all_triples_up_to_twenty(self):
        self.assertEqual(
            problem1.pythagorean_triples(20),
            [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20)],
        )


if __name__ == "__main__":
    unittest.main()

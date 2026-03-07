import unittest

def pythagorean_triples(n):
    return [
        (x, y, z)
        for x in range(1, n + 1)
        for y in range(x, n + 1)
        for z in range(y, n + 1)
        if x * x + y * y == z * z
    ]

class TestPythagoreanTriples(unittest.TestCase):

    def test_empty_for_small_n(self):
        self.assertEqual(pythagorean_triples(4), [])

    def test_known_triples(self):
        result = pythagorean_triples(20)
        self.assertIn((3, 4, 5), result)
        self.assertIn((5, 12, 13), result)
        self.assertIn((8, 15, 17), result)

    def test_equation_property(self):
        for x, y, z in pythagorean_triples(50):
            self.assertEqual(x*x + y*y, z*z)

    def test_order_property(self):
        for x, y, z in pythagorean_triples(50):
            self.assertTrue(x <= y <= z)

    def test_values_not_exceed_n(self):
        n = 30
        for x, y, z in pythagorean_triples(n):
            self.assertTrue(x <= n and y <= n and z <= n)

    def test_no_duplicates(self):
        triples = pythagorean_triples(50)
        self.assertEqual(len(triples), len(set(triples)))

if __name__ == "__main__":
    unittest.main()
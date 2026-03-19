from math import gcd, sqrt

def gen_triplets(n):
    return [
        (x, y, z)
        for x in range(1, n+1)
        for y in range(x, n+1)
        for z in [int(sqrt(x**2 + y**2))]
        if gcd(x, y) == 1
        and z <= n
        and z**2 == x**2 + y**2
    ]


if __name__ == "__main__":
    import unittest
    import random
    class TestGenTriplets(unittest.TestCase):
        def test_n_10(self):
            self.assertEqual(gen_triplets(10), [(3, 4, 5)])

        def test_n_20(self):
            expected = [(3, 4, 5), (5, 12, 13), (8, 15, 17)]
            self.assertEqual(gen_triplets(20), expected)

        def test_n_30(self):
            expected = [(3, 4, 5), (5, 12, 13), (7, 24, 25), (8, 15, 17), (20, 21, 29)]
            self.assertEqual(gen_triplets(30), expected)

        def test_n_50(self):
            result = gen_triplets(50)
            expected = [
                (3, 4, 5), (5, 12, 13), (7, 24, 25), (8, 15, 17), 
                (9, 40, 41), (12, 35, 37), (20, 21, 29),
            ]
            self.assertEqual(result, expected)

        def test_n_1_to_5(self):
            self.assertEqual(gen_triplets(1), [])
            self.assertEqual(gen_triplets(2), [])
            self.assertEqual(gen_triplets(3), [])
            self.assertEqual(gen_triplets(4), [])
            self.assertEqual(gen_triplets(5), [(3, 4, 5)])
            
        def test_negative(self):
            self.assertEqual(gen_triplets(-1), [])
            self.assertEqual(gen_triplets(-100), [])

        def test_gcd_condition(self):
            triplets = gen_triplets(50)
            for x, y, _ in triplets:
                self.assertEqual(gcd(x, y), 1)

        def test_pythagorean_condition(self):
            triplets = gen_triplets(100)
            for x, y, z in triplets:
                self.assertEqual(x**2 + y**2, z**2)

        def test_z_range(self):
            n = 50
            triplets = gen_triplets(n)
            for _, _, z in triplets:
                self.assertLessEqual(z, n)

        def test_ordering(self):
            triplets = gen_triplets(50)
            for x, y, z in triplets:
                self.assertLessEqual(x, y)
                self.assertLessEqual(y, z)

        def test_fuzzing_fixed_seed(self):
            random.seed(42)
            for _ in range(100):
                n = random.randint(1, 200)
                triplets = gen_triplets(n)
                for x, y, z in triplets:
                    self.assertTrue(x**2 + y**2 == z**2)
                    self.assertTrue(z <= n)
                    self.assertTrue(gcd(x, y) == 1)
                    self.assertTrue(x <= y)

        def test_triplet_uniqueness(self):
            triplets = gen_triplets(100)
            triplet_set = set(triplets)
            self.assertEqual(len(triplets), len(triplet_set))

    unittest.main()

# test_cumulative_sum_properties.py
import random
import unittest

from problem1 import cumulative_sum


class TestCumulativeSumProperties(unittest.TestCase):
    def test_example(self):
        self.assertEqual(cumulative_sum([1, 2, 3]), [0, 1, 3, 6])

    def test_empty(self):
        self.assertEqual(cumulative_sum([]), [0])

    def test_random_ints_properties(self):
        rng = random.Random(12345678109)

        for _ in range(500):
            n = rng.randint(0, 200)
            xs = [rng.randint(-1_000_000, 1_000_000) for _ in range(n)]
            xs_copy = xs.copy()

            out = cumulative_sum(xs)

            # функция не изменила подаваемый в нее лист
            self.assertEqual(xs, xs_copy)

            # длина и первый элемент
            self.assertEqual(len(out), len(xs) + 1)
            self.assertEqual(out[0], 0)

            # разности дают исходную последовательность
            for i, x in enumerate(xs):
                self.assertEqual(out[i + 1] - out[i], x)

            # последняя сумма равна сумме входа
            self.assertEqual(out[-1], sum(xs))


if __name__ == "__main__":
    unittest.main()

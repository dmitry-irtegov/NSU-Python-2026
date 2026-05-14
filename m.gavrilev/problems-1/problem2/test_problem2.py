#!/usr/bin/env python3

import inspect
import random
import unittest

from problem2 import clip_numbers


def assert_clip_invariants(test_case, source, result, lower, upper):
    test_case.assertEqual(len(source), len(result))

    for original, clipped in zip(source, result, strict=True):
        test_case.assertGreaterEqual(clipped, lower)
        test_case.assertLessEqual(clipped, upper)

        if original < lower:
            test_case.assertEqual(clipped, lower)
        elif original > upper:
            test_case.assertEqual(clipped, upper)
        else:
            test_case.assertEqual(clipped, original)


class TestClipNumbersBasic(unittest.TestCase):
    def test_clips_values_outside_range(self):
        result = list(clip_numbers([-5, 0, 3, 10], 1, 5))

        self.assertEqual([1, 1, 3, 5], result)

    def test_empty_sequence_returns_empty_list(self):
        result = list(clip_numbers([], -10, 10))

        self.assertEqual([], result)

    def test_boundary_values_are_preserved(self):
        result = list(clip_numbers([-3, -2, 0, 2, 3], -2, 2))

        self.assertEqual([-2, -2, 0, 2, 2], result)

    def test_does_not_modify_input_list(self):
        numbers = [-10, 0, 10]

        result = list(clip_numbers(numbers, -5, 5))

        self.assertEqual([-10, 0, 10], numbers)
        self.assertEqual([-5, 0, 5], result)
        self.assertIsNot(numbers, result)


class TestClipNumbersLazy(unittest.TestCase):
    def test_clip_numbers_returns_lazy_generator(self):
        result = clip_numbers([-10, 0, 10], -5, 5)

        self.assertTrue(inspect.isgenerator(result))
        self.assertEqual([-5, 0, 5], list(result))

    def test_clip_numbers_reads_source_lazily(self):
        def numbers():
            yield -10
            yield 0
            raise RuntimeError("source was read too far")

        result = clip_numbers(numbers(), -5, 5)

        self.assertEqual(-5, next(result))
        self.assertEqual(0, next(result))
        with self.assertRaises(RuntimeError):
            next(result)


class TestClipNumbersErrors(unittest.TestCase):
    def test_invalid_boundaries_raise_value_error(self):
        with self.assertRaises(ValueError):
            list(clip_numbers([1, 2, 3], 10, 1))


class TestClipNumbersRandom(unittest.TestCase):
    def test_large_reproducible_random_integers_match_reference(self):
        rng = random.Random(741_852)
        numbers = [rng.randint(-(10**9), 10**9) for _ in range(20_000)]
        lower = -12_345
        upper = 98_765

        result = list(clip_numbers(numbers, lower, upper))
        expected = [min(max(number, lower), upper) for number in numbers]

        self.assertEqual(expected, result)

    def test_large_reproducible_random_floats_satisfy_invariants(self):
        rng = random.Random(963_258)
        numbers = [rng.uniform(-1000.0, 1000.0) for _ in range(12_000)]
        lower = -12.5
        upper = 18.75

        result = list(clip_numbers(numbers, lower, upper))

        assert_clip_invariants(self, numbers, result, lower, upper)


if __name__ == "__main__":
    unittest.main()

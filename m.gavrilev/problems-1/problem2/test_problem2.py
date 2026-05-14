#!/usr/bin/env python3

import inspect
import random
import unittest
from collections.abc import Iterator, Sequence
from datetime import date

from problem2 import OrderedValue, clip_values


def assert_clip_invariants[ValueT: OrderedValue](
    test_case: unittest.TestCase,
    source: Sequence[ValueT],
    result: Sequence[ValueT],
    lower: ValueT,
    upper: ValueT,
) -> None:
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


class TestClipValuesBasic(unittest.TestCase):
    def test_clips_values_outside_range(self) -> None:
        result: list[int] = list(clip_values([-5, 0, 3, 10], 1, 5))

        self.assertEqual([1, 1, 3, 5], result)

    def test_empty_sequence_returns_empty_list(self) -> None:
        numbers: list[int] = []

        result: list[int] = list(clip_values(numbers, -10, 10))

        self.assertEqual([], result)

    def test_boundary_values_are_preserved(self) -> None:
        result: list[int] = list(clip_values([-3, -2, 0, 2, 3], -2, 2))

        self.assertEqual([-2, -2, 0, 2, 2], result)

    def test_does_not_modify_input_list(self) -> None:
        numbers: list[int] = [-10, 0, 10]

        result: list[int] = list(clip_values(numbers, -5, 5))

        self.assertEqual([-10, 0, 10], numbers)
        self.assertEqual([-5, 0, 5], result)
        self.assertIsNot(numbers, result)


class TestClipValuesLazy(unittest.TestCase):
    def test_clip_values_returns_lazy_generator(self) -> None:
        result: Iterator[int] = clip_values([-10, 0, 10], -5, 5)

        self.assertTrue(inspect.isgenerator(result))
        self.assertEqual([-5, 0, 5], list(result))

    def test_clip_values_reads_source_lazily(self) -> None:
        def numbers() -> Iterator[int]:
            yield -10
            yield 0
            raise RuntimeError("source was read too far")

        result: Iterator[int] = clip_values(numbers(), -5, 5)

        self.assertEqual(-5, next(result))
        self.assertEqual(0, next(result))
        with self.assertRaises(RuntimeError):
            next(result)


class TestClipValuesErrors(unittest.TestCase):
    def test_invalid_boundaries_raise_value_error(self) -> None:
        with self.assertRaises(ValueError):
            list(clip_values([1, 2, 3], 10, 1))


class TestClipValuesRandom(unittest.TestCase):
    def test_large_reproducible_random_integers_match_reference(self) -> None:
        rng: random.Random = random.Random(741_852)
        numbers: list[int] = [rng.randint(-(10**9), 10**9) for _ in range(20_000)]
        lower: int = -12_345
        upper: int = 98_765

        result: list[int] = list(clip_values(numbers, lower, upper))
        expected: list[int] = [min(max(number, lower), upper) for number in numbers]

        self.assertEqual(expected, result)

    def test_large_reproducible_random_floats_satisfy_invariants(self) -> None:
        rng: random.Random = random.Random(963_258)
        numbers: list[float] = [rng.uniform(-1000.0, 1000.0) for _ in range(12_000)]
        lower: float = -12.5
        upper: float = 18.75

        result: list[float] = list(clip_values(numbers, lower, upper))

        assert_clip_invariants(self, numbers, result, lower, upper)


class TestClipValuesComparableTypes(unittest.TestCase):
    def test_clips_strings(self) -> None:
        words: list[str] = ["ant", "cat", "wolf", "yak"]

        result: list[str] = list(clip_values(words, "cat", "wolf"))

        self.assertEqual(["cat", "cat", "wolf", "wolf"], result)

    def test_clips_dates(self) -> None:
        dates: list[date] = [
            date(2025, 12, 31),
            date(2026, 5, 14),
            date(2027, 1, 1),
        ]

        result: list[date] = list(
            clip_values(dates, date(2026, 1, 1), date(2026, 12, 31))
        )

        self.assertEqual(
            [date(2026, 1, 1), date(2026, 5, 14), date(2026, 12, 31)],
            result,
        )


if __name__ == "__main__":
    unittest.main()

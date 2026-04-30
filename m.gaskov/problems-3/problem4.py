import unittest


class CartesianPowerElement:
    _items = None
    _indices = None

    def __init__(self, items, n):
        self._items = tuple(items)

        if n < 0:
            raise ValueError("n must be non-negative")

        if len(self._items) == 0 and n > 0:
            raise ValueError("items must be non-empty")

        if len(set(self._items)) != len(self._items):
            raise ValueError("items must be unique")

        self._indices = [0] * n

    def current(self):
        return tuple(self._items[i] for i in self._indices)

    def next(self):
        if len(self._indices) == 0:
            return self

        for i in range(len(self._indices) - 1, -1, -1):
            self._indices[i] += 1

            if self._indices[i] < len(self._items):
                return self

            self._indices[i] = 0

        return self

    def __eq__(self, other):
        if not isinstance(other, CartesianPowerElement):
            return False

        return (
            self._items == other._items
            and self._indices == other._indices
        )


class TestCartesianPowerElement(unittest.TestCase):
    def test_current_initial(self):
        element = CartesianPowerElement((1, "a"), 2)
        self.assertEqual(element.current(), (1, 1))

    def test_next_once(self):
        element = CartesianPowerElement((1, "a"), 2)
        element.next()
        self.assertEqual(element.current(), (1, "a"))

    def test_next_twice(self):
        element = CartesianPowerElement((1, "a"), 2)
        element.next()
        element.next()
        self.assertEqual(element.current(), ("a", 1))

    def test_all_elements(self):
        element = CartesianPowerElement((1, "a"), 2)
        result = []

        for _ in range(4):
            result.append(element.current())
            element.next()

        self.assertEqual(
            result,
            [
                (1, 1),
                (1, "a"),
                ("a", 1),
                ("a", "a"),
            ]
        )

    def test_cycle(self):
        element = CartesianPowerElement((1, "a"), 2)

        for _ in range(4):
            element.next()

        self.assertEqual(element.current(), (1, 1))

    def test_cycle_more_than_one_round(self):
        element = CartesianPowerElement((1, "a"), 2)

        for _ in range(6):
            element.next()

        self.assertEqual(element.current(), ("a", 1))

    def test_three_items_power_two(self):
        element = CartesianPowerElement(("a", "b", "c"), 2)
        result = []

        for _ in range(9):
            result.append(element.current())
            element.next()

        self.assertEqual(
            result,
            [
                ("a", "a"),
                ("a", "b"),
                ("a", "c"),
                ("b", "a"),
                ("b", "b"),
                ("b", "c"),
                ("c", "a"),
                ("c", "b"),
                ("c", "c"),
            ]
        )

    def test_power_three(self):
        element = CartesianPowerElement((0, 1), 3)
        result = []

        for _ in range(8):
            result.append(element.current())
            element.next()

        self.assertEqual(
            result,
            [
                (0, 0, 0),
                (0, 0, 1),
                (0, 1, 0),
                (0, 1, 1),
                (1, 0, 0),
                (1, 0, 1),
                (1, 1, 0),
                (1, 1, 1),
            ]
        )

    def test_next_returns_self(self):
        element = CartesianPowerElement((1, 2), 2)
        self.assertEqual(element.next(), element)

    def test_power_zero(self):
        element = CartesianPowerElement((1, 2, 3), 0)
        self.assertEqual(element.current(), ())

    def test_power_zero_cycle(self):
        element = CartesianPowerElement((1, 2, 3), 0)
        element.next()
        element.next()
        self.assertEqual(element.current(), ())

    def test_create_from_iterator(self):
        items = (i for i in range(3))
        element = CartesianPowerElement(items, 2)
        self.assertEqual(element.current(), (0, 0))

    def test_empty_items_with_positive_power(self):
        with self.assertRaises(ValueError):
            CartesianPowerElement((), 2)

    def test_empty_items_with_zero_power(self):
        element = CartesianPowerElement((), 0)
        self.assertEqual(element.current(), ())

    def test_negative_power(self):
        with self.assertRaises(ValueError):
            CartesianPowerElement((1, 2), -1)

    def test_not_unique_items(self):
        with self.assertRaises(ValueError):
            CartesianPowerElement((1, 2, 1), 2)

    def test_equality(self):
        first = CartesianPowerElement((1, "a"), 2)
        second = CartesianPowerElement((1, "a"), 2)

        self.assertEqual(first, second)

        first.next()

        self.assertNotEqual(first, second)

    def test_equality_with_non_element(self):
        element = CartesianPowerElement((1, 2), 2)
        self.assertNotEqual(element, ((1, 1),))


if __name__ == "__main__":
    unittest.main()

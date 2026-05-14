import itertools
import unittest
import random


class CartesianProduct:
    def __init__(self, elements, n):
        self._product_list = list(elements)
        self._n = n
        self._iterator = itertools.cycle(
            itertools.product(self._product_list, repeat=self._n)
        )
        self._current = next(self._iterator)

    def get_current(self):
        return self._current

    def set_next(self):
        self._current = next(self._iterator)


class TestCartesianProduct(unittest.TestCase):

    def test_basic_logic(self):
        c = CartesianProduct([1, "a"], 2)
        self.assertEqual(c.get_current(), (1, 1))
        c.set_next()
        self.assertEqual(c.get_current(), (1, "a"))
        c.set_next()
        self.assertEqual(c.get_current(), ("a", 1))
        c.set_next()
        self.assertEqual(c.get_current(), ("a", "a"))
        c.set_next()
        self.assertEqual(c.get_current(), (1, 1))

    def test_random_elements(self):
        random.seed(42)
        for _ in range(5):
            elements = list(set(random.randint(0, 100) for _ in range(5)))
            n = random.randint(1, 3)

            c = CartesianProduct(elements, n)
            expected_first = tuple([elements[0]] * n)
            self.assertEqual(c.get_current(), expected_first)

    def test_large_product(self):
        n = 12
        elements = [0, 1]
        total_combinations = len(elements) ** n

        c = CartesianProduct(elements, n)

        for _ in range(total_combinations - 1):
            c.set_next()

        self.assertEqual(c.get_current(), tuple([1] * n))

        c.set_next()
        self.assertEqual(c.get_current(), tuple([0] * n))

    def test_single_element_set(self):
        c = CartesianProduct(["only"], 5)
        self.assertEqual(c.get_current(), ("only", "only", "only", "only", "only"))
        c.set_next()
        self.assertEqual(c.get_current(), ("only", "only", "only", "only", "only"))

    def test_n_is_zero(self):
        c = CartesianProduct([1, 2, 3], 0)
        self.assertEqual(c.get_current(), ())
        c.set_next()
        self.assertEqual(c.get_current(), ())


if __name__ == "__main__":
    unittest.main()

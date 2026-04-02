import unittest
from itertools import product as itertools_product

from problem3_4 import cartesian_power, CartesianProduct

def reference(elements, n):
    return list(itertools_product(elements, repeat=n))


class TestCartesianPowerOrder(unittest.TestCase):
    def test_example_from_task(self):
        result = list(cartesian_power([1, 'a'], 2))
        self.assertEqual(result, [(1, 1), (1, 'a'), ('a', 1), ('a', 'a')])

    def test_order_two_elements(self):
        result = list(cartesian_power([0, 1], 2))
        self.assertEqual(result, [(0, 0), (0, 1), (1, 0), (1, 1)])

    def test_order_three_elements_n2(self):
        result = list(cartesian_power([0, 1, 2], 2))
        expected = reference([0, 1, 2], 2)
        self.assertEqual(result, expected)

    def test_order_n3(self):
        result = list(cartesian_power([0, 1], 3))
        expected = reference([0, 1], 3)
        self.assertEqual(result, expected)


class TestCartesianPowerCount(unittest.TestCase):
    def test_n0_yields_one_empty_tuple(self):
        result = list(cartesian_power([1, 2, 3], 0))
        self.assertEqual(result, [()])

    def test_n1(self):
        result = list(cartesian_power([1, 'a'], 1))
        self.assertEqual(result, [(1,), ('a',)])

    def test_count_matches_power(self):
        for size in [1, 2, 3, 4]:
            X = list(range(size))
            for n in range(5):
                with self.subTest(size=size, n=n):
                    count = sum(1 for _ in cartesian_power(X, n))
                    self.assertEqual(count, size ** n)

    def test_n_greater_than_len_x(self):
        result = list(cartesian_power([0, 1], 3))
        expected = reference([0, 1], 3)
        self.assertEqual(result, expected)

    def test_single_element_set(self):
        result = list(cartesian_power(['x'], 4))
        self.assertEqual(result, [('x', 'x', 'x', 'x')])


class TestCartesianPowerUniqueness(unittest.TestCase):

    def test_no_duplicates(self):
        result = list(cartesian_power([1, 2, 3], 3))
        self.assertEqual(len(result), len(set(result)))

class TestCartesianProductInitialValue(unittest.TestCase):

    def test_initial_value_is_first_element(self):
        cp = CartesianProduct([1, 'a'], 2)
        self.assertEqual(cp.value(), (1, 1))

    def test_value_unchanged_without_next(self):
        cp = CartesianProduct([1, 2], 2)
        for _ in range(10):
            self.assertEqual(cp.value(), (1, 1))

    def test_initial_value_n0(self):
        cp = CartesianProduct([1, 2], 0)
        self.assertEqual(cp.value(), ())


class TestCartesianProductSequentialTraversal(unittest.TestCase):

    def _collect(self, cp, count):
        results = [cp.value()]
        for _ in range(count - 1):
            cp.next()
            results.append(cp.value())
        return results

    def test_full_traversal_n2(self):
        cp = CartesianProduct([1, 'a'], 2)
        expected = [(1, 1), (1, 'a'), ('a', 1), ('a', 'a')]
        self.assertEqual(self._collect(cp, 4), expected)

    def test_full_traversal_n1(self):
        cp = CartesianProduct(['a', 'b', 'c'], 1)
        expected = [('a',), ('b',), ('c',)]
        self.assertEqual(self._collect(cp, 3), expected)

    def test_full_traversal_matches_reference(self):
        X = [0, 1, 2]
        n = 3
        cp = CartesianProduct(X, n)
        expected = reference(X, n)
        self.assertEqual(self._collect(cp, len(expected)), expected)


class TestCartesianProductCycling(unittest.TestCase):
    def test_wrap_after_full_cycle(self):
        cp = CartesianProduct([1, 'a'], 2)
        for _ in range(4):
            cp.next()
        self.assertEqual(cp.value(), (1, 1))

    def test_multiple_full_cycles(self):
        X = [0, 1]
        n = 2
        cp = CartesianProduct(X, n)
        expected = reference(X, n)
        for cycle in range(3):
            for step, elem in enumerate(expected):
                with self.subTest(cycle=cycle, step=step):
                    self.assertEqual(cp.value(), elem)
                cp.next()

    def test_n0_cycle(self):
        cp = CartesianProduct([1, 2, 3], 0)
        for _ in range(5):
            self.assertEqual(cp.value(), ())
            cp.next()


class TestCartesianProductIsolation(unittest.TestCase):
    def test_mutation_of_source_list_has_no_effect(self):
        X = [1, 2]
        cp = CartesianProduct(X, 2)
        X.append(99)
        results = [cp.value()]
        for _ in range(3):
            cp.next()
            results.append(cp.value())
        self.assertEqual(results, [(1, 1), (1, 2), (2, 1), (2, 2)])

    def test_two_independent_instances(self):
        cp1 = CartesianProduct([0, 1], 2)
        cp2 = CartesianProduct([0, 1], 2)
        cp1.next()
        cp1.next()
        self.assertEqual(cp2.value(), (0, 0))
        self.assertEqual(cp1.value(), (1, 0))

    def test_heterogeneous_elements(self):
        cp = CartesianProduct([None, True, 3.14], 1)
        self.assertEqual(cp.value(), (None,))
        cp.next()
        self.assertEqual(cp.value(), (True,))
        cp.next()
        self.assertEqual(cp.value(), (3.14,))


if __name__ == '__main__':
    unittest.main()
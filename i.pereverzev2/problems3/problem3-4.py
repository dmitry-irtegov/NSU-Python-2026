import unittest

class CartesianCounter:
    def __init__(self, elements, n):
        self.elements = list(elements)
        self.n = n
        self.indices = [0] * n

    def get_current(self):
        return tuple(self.elements[i] for i in self.indices)

    def set_next(self):
        for i in range(self.n - 1, -1, -1):
            self.indices[i] += 1
            if self.indices[i] < len(self.elements):
                break
            self.indices[i] = 0


class TestCartesianCounter(unittest.TestCase):
    def test_basic_example(self):
        c = CartesianCounter([1, 'a'], 2)
        
        self.assertEqual(c.get_current(), (1, 1))
        c.set_next()
        self.assertEqual(c.get_current(), (1, 'a'))
        c.set_next()
        self.assertEqual(c.get_current(), ('a', 1))
        c.set_next()
        self.assertEqual(c.get_current(), ('a', 'a'))

    def test_cycling(self):
        c = CartesianCounter([1, 'a'], 2)
        
        for _ in range(4):
            c.set_next()
            
        self.assertEqual(c.get_current(), (1, 1))

    def test_n_equals_1(self):
        c = CartesianCounter(['x', 'y', 'z'], 1)
        
        self.assertEqual(c.get_current(), ('x',))
        c.set_next()
        self.assertEqual(c.get_current(), ('y',))
        c.set_next()
        self.assertEqual(c.get_current(), ('z',))
        c.set_next()
        self.assertEqual(c.get_current(), ('x',))

    def test_n_equals_3(self):
        c = CartesianCounter([0, 1], 3)
        expected = [
            (0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1),
            (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)
        ]
        
        for exp in expected:
            self.assertEqual(c.get_current(), exp)
            c.set_next()
            
        self.assertEqual(c.get_current(), (0, 0, 0))

if __name__ == '__main__':
    unittest.main()
def cartesian_power(elements, n):
    items = list(elements)
    if n == 0:
        yield ()
        return

    indices = [0] * n
    while True:
        yield tuple(items[i] for i in indices)

        j = 0
        while j < len(items) and indices[j] == len(items) - 1:
            j += 1

        if j == len(items):
            break

        indices[j] += 1
        for k in range(j + 1, n):
            indices[k] = 0

class CartesianProduct:
    def __init__(self, X, n):
        self._X = X.copy()
        self._n = n
        self._elements = cartesian_power(X, n)
        self._value = next(self._elements)

    def value(self):
        return self._value

    def next(self):
        self._value = next(self._elements, None)

        if self._value is None:
            self._elements = cartesian_power(self._X, self._n)
            self._value = next(self._elements)
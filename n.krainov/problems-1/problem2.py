def apply_boundaries(numList, a, b):
    res = map(lambda x: a if x < a else b if x > b else x, numList)

    return list(res)

assert apply_boundaries([1, 2, 3], 2, 2) == [2, 2, 2]
assert apply_boundaries([7, 12, 3, 5345, -123], -1, 5346) == [7, 12, 3, 5345, -1]
def bounds(lower_bound, upper_bound, nums):
    res = map(lambda x: lower_bound if x < lower_bound else upper_bound if x > upper_bound else x, nums)
    return list(res)

assert (bounds(1, 3, [0, 2, 4]) == [1, 2, 3])
assert (bounds(0, 0, [1, -1, 5]) == [0, 0, 0])
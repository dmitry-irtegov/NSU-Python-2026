def bounds(lower_bound, upper_bound, nums):
    res = map(lambda x: lower_bound if x < lower_bound else upper_bound if x > upper_bound else x, nums)
    return list(res)


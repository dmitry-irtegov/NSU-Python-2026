def cumulative_sum(arr):
    res = [0]
    s = 0
    for x in arr:
        s += x
        res.append(s)
    return res
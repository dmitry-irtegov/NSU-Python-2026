def cumulative_sum(numList):
    if len(numList) == 0:
        return [0]

    res = [0]
    for i in range(len(numList)):
        res.append(res[-1] + numList[i])

    return res

assert cumulative_sum([10, 20, 30]) == [0, 10, 30, 60]
assert cumulative_sum([0]) == [0, 0]
assert cumulative_sum([]) == [0]
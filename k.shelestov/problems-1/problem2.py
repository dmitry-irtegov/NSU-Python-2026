def clip_numbers(seq, lower_bound, upper_bound):
    res = []
    for num in seq:
        if num < lower_bound:
            res.append(lower_bound)
        elif num > upper_bound:
            res.append(upper_bound)
        else:
            res.append(num)
    return res


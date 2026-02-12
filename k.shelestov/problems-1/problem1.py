def cumsum(seq):
    cumulative_sum = [0]
    current_sum = 0
    for num in seq:
        current_sum += num
        cumulative_sum.append(current_sum)
    return cumulative_sum

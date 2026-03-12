def cumulative_sum(arr: list[int]) -> list[int]:
    result = [0]
    total = 0
    for number in arr:
        total += number
        result.append(total)
    return result

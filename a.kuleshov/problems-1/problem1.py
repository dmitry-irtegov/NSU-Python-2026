nums = list(map(int, input("Введите числа через пробел: ").split()))

def cumulative_sums(seq):
    result = [0]
    total = 0

    for x in seq:
        total += x
        result.append(total)

    return result

result = cumulative_sums(nums)

print(result)
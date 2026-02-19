def acc_sums(numbers):
    result = [0]
    for i in range(len(numbers)):
        result.append(result[i] + numbers[i])
    return result


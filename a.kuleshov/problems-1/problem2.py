def clip_sequence(seq, a, b):
    result = []

    for x in seq:
        if x < a:
            result.append(a)
        elif x > b:
            result.append(b)
        else:
            result.append(x)

    return result

nums = list(map(int, input("Введите числа через пробел: ").split()))

a, b = map(int, input("Введите a и b через пробел: ").split())

clipped = clip_sequence(nums, a, b)

print(clipped)
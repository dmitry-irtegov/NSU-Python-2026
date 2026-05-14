def clip_sequence(numbers, a, b):
    if a > b:
        raise ValueError("Lower bound must be greate than upper bound")
    return [max(a, min(x, b)) for x in numbers]


if __name__ == "__main__":
    try:
        numbers_line = input("Enter the numbers: ")
        numbers = [int(x) for x in numbers_line.split()]
        a = int(input("Lower bound a: "))
        b = int(input("Upper bound b: "))
        result = clip_sequence(numbers, a, b)
        print(result)
    except ValueError as e:
        print("Wrong input:", e)

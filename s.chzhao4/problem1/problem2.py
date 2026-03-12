def clip_numbers(nums: list[int], a: int, b: int) -> list[int]:
    result = []
    for x in nums:
        if x < a:
            result.append(a)
        elif x > b:
            result.append(b)
        else:
            result.append(x)
    return result

if __name__ == "__main__":
    print(clip_numbers([1, 5, 10, 4], 3, 7))

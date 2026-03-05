def cumulative_sum(nums: list[int]) -> list[int]:
    result = [0]
    current_sum = 0
    for num in nums:
        current_sum += num
        result.append(current_sum)
    return result

if __name__ == "__main__":
    print(cumulative_sum([1, 2, 3]))
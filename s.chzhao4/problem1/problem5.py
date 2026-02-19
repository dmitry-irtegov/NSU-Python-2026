def prime_factors(n: int) -> list[list[int]]:
    factors = []
    divisor = 2
    temp = n

    while divisor * divisor <= temp:
        if temp % divisor == 0:
            count = 0
            while temp % divisor == 0:
                count += 1
                temp //= divisor
            factors.append([divisor, count])
        divisor += 1

    # 如果最后剩下一个大于1的数，那它本身就是质数
    if temp > 1:
        factors.append([temp, 1])

    return factors

if __name__ == "__main__":
    print(prime_factors(12))  # [[2, 2], [3, 1]]
    print(prime_factors(100))  # [[2, 2], [5, 2]]
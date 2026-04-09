def prime_factors(n: int) -> list[tuple[int, int]]:
    if n < 2:
        return []

    factors = []
    temp = n

    if temp % 2 == 0:
        count = 0
        while temp % 2 == 0:
            count += 1
            temp //= 2
        factors.append((2, count))

    divisor = 3
    while divisor * divisor <= temp:
        if temp % divisor == 0:
            count = 0
            while temp % divisor == 0:
                count += 1
                temp //= divisor
            factors.append((divisor, count))
        divisor += 2

    if temp > 1:
        factors.append((temp, 1))

    return factors

if __name__ == "__main__":
    print(f"12 : {prime_factors(12)}")
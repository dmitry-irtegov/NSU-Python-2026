def prime_factors(n):
    factors = []
    d = 2

    while d * d <= n:
        count = 0

        while n % d == 0:
            n //= d
            count += 1

        if count > 0:
            factors.append([d, count])

        d += 1

    if n > 1:
        factors.append([n, 1])

    return factors

num = int(input("Введите число: "))

result = prime_factors(num)

print(result)

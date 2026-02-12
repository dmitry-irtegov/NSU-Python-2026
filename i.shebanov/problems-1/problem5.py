def prime_divisors(n):
    result = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            count = 0
            while n % i == 0:
                count += 1
                n //= i
            result.append([i, count])
        i += 1
    if n != 1:
        result.append([n, 1])
    return result

n = int(input())

primes_list = [
        i for i in range(2, n + 1)
        if all(i % j for j in range(2, int((i)**0.5) + 1))
    ]
print(primes_list)
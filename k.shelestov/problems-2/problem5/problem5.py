def return_prime_list(n):
    return [
        x for x in range(2, n + 1)
        if all(x % d != 0 for d in range(2, int(x ** 0.5) + 1))
    ]
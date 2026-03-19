from math import gcd


def primitive_pythagorean_triples(limit: int):
    triples = [
        tuple(sorted((m*m - n*n, 2*m*n, m*m + n*n)))
        for m in range(2, int(limit**0.5) + 2)
        for n in range(1, m)
        if gcd(m, n) == 1
        and (m - n) % 2 == 1
        and m*m + n*n <= limit
    ]

    return sorted(triples)
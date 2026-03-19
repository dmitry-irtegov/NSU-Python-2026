import math

def pythagorean_triples(limit):
    if limit <= 0:
        raise ValueError("limit must be greater than 0")

    triples = []
    max_m = int(math.isqrt(limit)) + 1

    #Euclid's formula
    for m in range(2, max_m):
        for n in range(1, m):
            c0 = m * m + n * n
            if c0 > limit:
                continue

            if math.gcd(m, n) != 1 or (m % 2 == n % 2):
                continue

            a0 = m * m - n * n
            b0 = 2 * m * n

            if a0 > b0:
                a0, b0 = b0, a0

            k = 1
            while True:
                a = k * a0
                b = k * b0
                c = k * c0
                if c > limit:
                    break
                triples.append((a, b, c))
                k += 1

    return triples

if __name__ == '__main__':
    try:
        limit = int(input("Please enter the limit: "))
        print(pythagorean_triples(limit))
    except Exception as e:
        print("error occurred: ", str(e))
        exit(1)
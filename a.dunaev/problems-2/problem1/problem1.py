def pythagorean_triples(n):
    return [
        (x, y, z)
        for z in range(1, n + 1)
        for y in range(1, z + 1)
        for x in range(1, y + 1)
        if x * x + y * y == z * z
    ]

if __name__ == "__main__":
    print(pythagorean_triples(10))
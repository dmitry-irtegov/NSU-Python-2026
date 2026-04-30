def pythagorean_triples(n: int) -> list[tuple[int, int, int]]:
    return [
        (x, y, z)
        for x in range(1, n + 1)
        for y in range(x, n + 1)
        for z in range(y, n + 1)
        if x * x + y * y == z * z
    ]

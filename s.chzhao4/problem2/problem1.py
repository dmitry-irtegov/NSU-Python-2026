n = 30

pythagorean_triples = [
    (x, y, z)
    for x in range(1, n + 1)
    for y in range(x, n + 1)
    for z in range(y, n + 1)
    if x**2 + y**2 == z**2
]

print(f"n={n} 以内的勾股数: {pythagorean_triples}")
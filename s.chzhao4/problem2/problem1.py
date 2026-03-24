def generate_pythagorean_triples(n: int) -> list:
    if n < 5:
        return []

    return [(x, y, z)
            for x in range(1, n)
            for y in range(x + 1, n)
            for z in range(y + 1, n + 1)
            if x**2 + y**2 == z**2]

if __name__ == "__main__":
    try:
        user_input = int(input("Please enter the maximum range n:"))
        triples = generate_pythagorean_triples(user_input)
        for t in triples:
            print(t)
    except ValueError:
        print("Invalid input:")
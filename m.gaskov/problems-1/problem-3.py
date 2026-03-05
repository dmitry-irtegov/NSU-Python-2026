def collatz_chain(n: int) -> list[int]:
    if n <= 0:
        raise ValueError("n must be a positive integer")

    chain = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        chain.append(n)
    return chain


def main():
    s = input().strip()
    n = int(s)
    chain = collatz_chain(n)
    print(" -> ".join(map(str, chain)))


if __name__ == "__main__":
    main()
def factorize(number: int) -> list[list[int]]:
    if number <= 1:
        return []

    res: list[list[int]] = []
    p = 2
    while p * p <= number:
        if number % p == 0:
            k = 0
            while number % p == 0:
                number = number // p
                k = k + 1
            res.append([p, k])
        p += 1 if p == 2 else 2
    if number > 1:
        res.append([number, 1])
    return res


def main() -> None:
    try:
        number = int(input())
    except ValueError:
        return
    print(factorize(number))


if __name__ == "__main__":
    main()

def collatz(number: int) -> list[int]:
    if number <= 0:
        return []

    res = [number]
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        res.append(number)
    return res


def main() -> None:
    try:
        number = int(input())
    except ValueError:
        return
    arr = collatz(number)
    if arr:
        print(arr[0], end="")
        for x in arr[1:]:
            print(" ->", x, end="")
        print()


if __name__ == "__main__":
    main()

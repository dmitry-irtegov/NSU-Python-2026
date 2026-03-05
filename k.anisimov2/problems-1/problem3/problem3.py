import sys


def collatz(number):
    if number <= 0:
        print(f"Invalid number for Collatz: {number}. Expected a positive integer.", file=sys.stderr)
        return []

    res = [number]
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        res.append(number)
    return res


def main():
    try:
        raw = input()
        number = int(raw)
    except KeyboardInterrupt:
        print("Interrupted by user.", file=sys.stderr)
        return
    except Exception as e:
        print(f"Input error: {e}", file=sys.stderr)
        return

    arr = collatz(number)
    if not arr:
        return

    print(arr[0], end="")
    for x in arr[1:]:
        print(" ->", x, end="")
    print()


if __name__ == "__main__":
    main()
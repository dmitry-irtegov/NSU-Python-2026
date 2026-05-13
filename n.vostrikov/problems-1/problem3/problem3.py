def collatz(num: int):
    if num <= 0:
        return []
    while num != 1:
        print(num, end="->")
        num = num // 2 if not (num % 2) else 3 * num + 1
    print(num)


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    collatz(n)

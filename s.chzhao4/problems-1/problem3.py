def collatz_conjecture() -> None:
    try:
        n = int(input("输入一个数字: "))
    except ValueError:
        print("请输入有效的")
        return

    sequence = []
    while n != 1:
        sequence.append(str(n))
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

    sequence.append("1")
    print(" -> ".join(sequence))


if __name__ == "__main__":
    collatz_conjecture()
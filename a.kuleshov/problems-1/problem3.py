if __name__ == "__main__":
    n = int(input())

    sequence = [n]

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        sequence.append(n)

    print(*sequence, sep=" -> ")
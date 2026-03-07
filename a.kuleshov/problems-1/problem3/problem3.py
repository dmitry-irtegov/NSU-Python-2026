def collatz_sequence(n: int):
    sequence = [n]

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        sequence.append(n)

    return sequence

def main():
    n = int(input())
    sequence = collatz_sequence(n)
    print(*sequence, sep=" -> ")

if __name__ == "__main__":
    main()
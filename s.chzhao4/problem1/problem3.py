def collatz_conjecture(n: int) -> list:
    if n <= 0:
        raise ValueError("The Collatz conjecture only applies to positive integers greater than 0.")

    sequence = []
    while n != 1:
        sequence.append(str(n))
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

    sequence.append("1")
    return sequence


def main():
    user_input = input("Enter a number:")
    try:
        n = int(user_input)

        result_sequence = collatz_conjecture(n)

        print(" -> ".join(result_sequence))

    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
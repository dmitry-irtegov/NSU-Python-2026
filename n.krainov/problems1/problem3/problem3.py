def print_collatz_seq(number):
    n = number
    i = 0
    print(n, end="")
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        i += 1
        print(" -> " + str(n), end="")


if __name__ == '__main__':
    import sys

    try:
        num = input("Enter a number: ")

        num = int(num)
        print_collatz_seq(num)
    except Exception as e:
        sys.stderr.write("Error occurred: " + str(e))
        exit(1)
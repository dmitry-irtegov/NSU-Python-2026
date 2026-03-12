def print_collatz_seq(number, maxIter = 1 << 61):
    seq = [number]
    n = number
    i = 0
    while n != 1:
        if i == maxIter:
            print("[]")
            return

        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        i += 1
        seq.append(n)

    print(' -> '.join(str(n) for n in seq))


if __name__ == '__main__':
    import sys

    try:
        num = input("Enter a number: ")

        num = int(num)
        print_collatz_seq(num)
    except Exception as e:
        sys.stderr.write("Error occurred: " + str(e))
        exit(1)
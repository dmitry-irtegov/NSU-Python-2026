def collatz_seq(number, maxIter = 1 << 61):
    seq = [number]
    n = number
    i = 0
    while n != 1:
        if i == maxIter:
            return False, []

        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        i += 1
        seq.append(n)

    return True, seq

original_print = print
def print(*args, **kwargs):
    new_args = []
    for arg in args:
        if isinstance(arg, tuple) and len(arg) == 2:
            first, second = arg
            if isinstance(first, bool) and isinstance(second, list):
                new_args.append(str(first) + " " + ' -> '.join(str(x) for x in second))
            else:
                new_args.append(arg)
        else:
            new_args.append(arg)
    original_print(*new_args, **kwargs)



assert collatz_seq(3) == (True, [3, 10, 5, 16, 8, 4, 2, 1])

if __name__ == '__main__':
    num = input("Enter a number: ")

    if num.isdigit():
        num = int(num)
        print(collatz_seq(num))
    else:
        print("it isn't a number")
from sys import argv, stderr

def hyp(num: int):
    if (num < 1):
        raise ValueError(f"trying to check hypotheses with num < 1 ({num})")

    while num != 1:
        print(f'{num}->', end="")
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 +1
    print('1')


if __name__ == '__main__':

    if len(argv) < 2:
        print("No num to check", file=stderr)
        exit(1)

    try:
        hyp(int(argv[1]))
    except ValueError as e:
        print(f"Invalid number: {e}", file=stderr)
        exit(1)
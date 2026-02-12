from sys import argv, stderr

def get_simple(number: int):
    number = abs(number)
    res = []
    for pretendent in range(2, number//2):
        if number % pretendent == 0:
            counter = 0
            while number % pretendent == 0:
                counter += 1
                number /= pretendent
            res.append([pretendent, counter])
    if number > 1:
        res.append([int(number), 1])
    return res

if len(argv) < 2:
    print(f'No numbers to work with', file=stderr)
    exit(1)



for i, arg in enumerate(argv[1:]):
    try:
        number = int(arg)
        res_list = get_simple(number)
        print(f'{arg} -> {res_list}\n')
    except ValueError:
        print(f'i = {i} number is not an integer or number at all = {arg}', file=stderr)
        exit(1)


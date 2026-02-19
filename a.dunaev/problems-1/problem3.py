#!/usr/bin/python

orig_print = print
buffer = ""

def custom_print(*args, end="\n"):
    global buffer

    for i in args:
        buffer += str(i) + end

print = custom_print

def program(inp: int) -> None:
    while inp > 1:
        print(inp, end=" -> ")
        inp = inp // 2 if inp % 2 == 0 else 3 * inp + 1

    print(inp)

def test():
    from random import randint

    def test_case():
        num = randint(1, 100)
        program(num)
        res = buffer.split('\n')[-2].split(' -> ')
        assert res[0] == str(num) and res[-1] == "1"


    for i in range(100):
        test_case()

if __name__ == "__main__":
    test()

print = orig_print

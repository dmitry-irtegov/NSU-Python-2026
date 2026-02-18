inp = int(input())

while inp > 1:
    print(inp, end=" -> ")
    inp = inp // 2 if inp % 2 == 0 else 3 * inp + 1

print(inp)
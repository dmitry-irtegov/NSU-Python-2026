#!/usr/bin/python
def collatz(inp):
    if inp < 1:
        raise ValueError("inp must be positive")

    result = [inp]
    while inp > 1:
        inp = inp // 2 if inp % 2 == 0 else 3 * inp + 1
        result.append(inp)

    return result


def format_seq(inp):
    return " -> ".join(map(str, collatz(inp)))

def main():
    print(format_seq(7))


if __name__ == "__main__":
    main()

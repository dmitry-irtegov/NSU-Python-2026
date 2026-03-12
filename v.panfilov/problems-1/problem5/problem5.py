#!/usr/bin/env python3.12
from sys import stderr, exit

def prime_factors(n: int) -> list[list[int]]:
    """
    Разлагает число n на простые множители и возвращает список пар [множитель, степень].

    Аргументы:
        n: целое число (n > 1 для содержательного разложения)

    Возвращает:
        Список вида [[p1, k1], [p2, k2], ...], где p_i — простые множители,
        k_i — их степени.
    """
    if not isinstance(n, int):
        raise ValueError("Number must be an Int.")

    if n < 1:
        raise ValueError("Number must be > zero.")

    if n == 1:
        return [[1, 1]]
    result = []
    multiplier = 2
    while multiplier * multiplier <= n:
        pow = 0
        while n % multiplier == 0:
            pow += 1
            n //= multiplier
        if pow > 0:
            result.append([multiplier, pow])
        else:
            multiplier += 1
    if n >= 1:
        result.append([n, 1])
    return result


if __name__ == '__main__':
    while True:
        try:
            a = int(input('Enter number: '))
            result = prime_factors(a)
            print(result)
            break
        except ValueError as e:
            print(f"Value error received:\n{e}", file=stderr)
        except KeyboardInterrupt:
            print("KeyboardInterrupt received", file=stderr)
            exit()
        except EOFError:
            print("EOFError received", file=stderr)
            exit()
        except Exception as e:
            print(f"Ошибка:\n{e}", file=stderr)
            exit()

#!/usr/bin/env python3.12

from sys import stderr, exit


def collatz_sequence(n: int):
    """
    Возвращает последовательность Коллатца для заданного числа n.
    Последовательность заканчивается числом 1.
    """
    if n <= 0:
        raise ValueError("Число должно быть положительным")
    seq = [n]
    try:
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            seq.append(n)
        return seq
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == '__main__':
    """Основная функция программы."""
    while True:
        try:
            user_input = input("Введите натуральное число: ")
            n = int(user_input)
            sequence = collatz_sequence(n)
            print(" → ".join(map(str, sequence)))
            break
        except ValueError as e:
            print(f"Ошибка: {e}", file=stderr)
        except KeyboardInterrupt:
            print("KeyboardInterrupt received", file=stderr)
            exit()
        except EOFError:
            print("EOFError received", file=stderr)
            exit()
        except Exception as e:
            print(f"Ошибка:\n {e}", file=stderr)
            exit()
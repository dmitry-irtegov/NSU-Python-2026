import math
import sys


def get_primes(n: int) -> list[int]:
    return [
        x for x in range(2, n + 1)
        if all(x % d != 0 for d in range(2, math.isqrt(x) + 1))
    ]


def main() -> None:
    print("Введите максимальное число (N) для поиска простых чисел:")
    try:
        user_input: str = input("> ").strip()
        if not user_input:
            return

        n: int = int(user_input)
        if n < 2:
            print("Нет простых чисел в заданном диапазоне.")
            return

        primes: list[int] = get_primes(n)
        print(f"Найдено простых чисел: {len(primes)}")
        print(f"Простые числа: {primes}")

    except ValueError:
        print("Ошибка: Пожалуйста, введите целое число.")
        sys.exit(1)
    except (EOFError, KeyboardInterrupt):
        print()
        sys.exit(0)


if __name__ == "__main__":
    main()
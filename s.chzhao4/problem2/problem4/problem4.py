import os
import sys


def find_all_occurrences(text: str, sub: str) -> list[int]:
    positions: list[int] = []
    start: int = 0
    while True:
        idx: int = text.find(sub, start)
        if idx == -1:
            break
        positions.append(idx)
        start = idx + 1

    return positions


def main() -> None:
    base_dir: str = os.path.dirname(os.path.abspath(__file__))
    file_path: str = os.path.join(base_dir, "pi.txt")

    if not os.path.exists(file_path):
        print(f"Ошибка: Файл '{file_path}' не найден. Пожалуйста, поместите pi.txt в папку со скриптом.")
        sys.exit(1)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            pi_data: str = f.read().strip()
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        sys.exit(1)

    print("Enter sequence to search for.")
    try:
        search_seq: str = input("> ").strip()
    except (EOFError, KeyboardInterrupt):
        print()
        sys.exit(0)

    if not search_seq:
        print("Введена пустая строка. Поиск отменен.")
        return

    positions: list[int] = find_all_occurrences(pi_data, search_seq)
    count: int = len(positions)

    print(f"Found {count} results.")

    if count > 0:
        first_five: list[str] = [str(p) for p in positions[:5]]
        positions_str: str = " ".join(first_five)

        if count > 5:
            print(f"Positions: {positions_str} ...")
        else:
            print(f"Positions: {positions_str}")

if __name__ == "__main__":
    main()
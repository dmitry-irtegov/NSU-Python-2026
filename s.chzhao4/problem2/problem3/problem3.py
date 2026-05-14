import os
import sys


def get_sorted_files(dir_path: str) -> list[tuple[str, int]]:
    if not os.path.isdir(dir_path):
        raise ValueError(f"Путь '{dir_path}' не является директорией или не существует.")

    files_info: list[tuple[str, int]] = []

    for filename in os.listdir(dir_path):
        full_path: str = os.path.join(dir_path, filename)

        if os.path.isfile(full_path):
            file_size: int = os.stat(full_path).st_size
            files_info.append((filename, file_size))

    files_info.sort(key=lambda x: (-x[1], x[0]))

    return files_info


def main() -> None:
    if len(sys.argv) != 2:
        print("Использование: python problem3.py <путь_к_директории>")
        sys.exit(1)

    dir_path: str = sys.argv[1]

    try:
        sorted_files: list[tuple[str, int]] = get_sorted_files(dir_path)
        for filename, size in sorted_files:
            print(f"{filename} - {size} bytes")
    except ValueError as e:
        print(f"Ошибка: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
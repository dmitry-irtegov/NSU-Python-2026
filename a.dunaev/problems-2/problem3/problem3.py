import os
import sys
from os.path import isfile, join


def get_sorted_files(directory):
    files = [
        (filename, os.stat(join(directory, filename)).st_size)
        for filename in os.listdir(directory)
        if isfile(join(directory, filename))
    ]
    return sorted(files, key=lambda file_info: (-file_info[1], file_info[0]))


def format_files(files):
    return "\n".join(f"{filename} {size}" for filename, size in files)


def main() -> None:
    print(format_files(get_sorted_files(sys.argv[1])))


if __name__ == "__main__":
    main()

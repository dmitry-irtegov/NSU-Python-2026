#!/usr/bin/env python3

from os import listdir, stat
from os.path import isfile, join
from sys import stderr, argv


def get_sorted_files(directory_path):
    files = []
    for item in listdir(directory_path):
        full_path = join(directory_path, item)
        if isfile(full_path):
            files.append((item, stat(full_path).st_size))
    return sorted(files, key=lambda x: (-x[1], x[0]))


if __name__ == "__main__":
    try:
        result = get_sorted_files(argv[1])
        for name, size in result:
            print(f"{name} - {size}")
    except KeyboardInterrupt:
        print("Shutting down...")
    except Exception as e:
        print(f"Exception in main(): {e}", file=stderr)

import os
import argparse
from os.path import isfile, join

def list_files_sorted(directory):
    files = []

    for name in os.listdir(directory):
        path = join(directory, name)

        if isfile(path):
            size = os.stat(path).st_size
            files.append((name, size))

    files.sort(key=lambda x: (-x[1], x[0]))

    return files

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")

    args = parser.parse_args()

    files = list_files_sorted(args.directory)

    for name, size in files:
        print(f"{name} {size}")

if __name__ == "__main__":
    main()
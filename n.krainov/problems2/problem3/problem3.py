import os
import sys

def get_sorted_files(directory):
    files = []
    for entry in os.listdir(directory):
        path = os.path.join(directory, entry)
        if os.path.isfile(path):
            size = os.path.getsize(path)
            files.append((entry, size))

    files.sort(key=lambda x: (x[1], x[0]))
    return files

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        exit(1)

    path = sys.argv[1]
    if not os.path.exists(path):
        print("The specified path does not exist")
        sys.exit(1)

    if not os.path.isdir(path):
        print("The specified path is not a directory")
        sys.exit(1)

    try:
        sorted_files = get_sorted_files(path)
    except Exception as e:
        print("Error occurred: ", e)
        exit(1)

    print("files:")
    for name, size in sorted_files:
        print(f"\t{name}: {size} bytes")
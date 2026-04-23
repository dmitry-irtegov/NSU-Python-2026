from os import listdir, stat
from os.path import isfile, join, isdir
from sys import argv, stderr


def main(path):
    """function that prints files and their sizes in directory from path
    files are being sorted by size in descending order; in case of same sizes files are sorted by alphabet order
    path - path to directory
    """
    
    if not(isdir(path)):
        print(f'Wrong path - {path} not a directory', file=stderr)
        return
    
    files_list = []
    try:
        for i in sorted(listdir(path)):
            name = join(path, i)
            if isfile(name):
                files_list.append((name, stat(name).st_size))
    except OSError as err:
        print("OSError: ", err, file=stderr)

    files_list = sorted(files_list, key=lambda file: -file[1])

    for (name, size) in files_list:
        print(name, size)

if __name__ == "__main__":
    if (len(argv) != 2):
        print("usage: python problem3.py <path_to_file>", file=stderr)
    else:
        main(argv[1])
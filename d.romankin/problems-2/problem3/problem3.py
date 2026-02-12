from os import listdir, stat
from os.path import isfile, join
from sys import argv, stderr


def main(path):
    
    
    path
    files_list = []
    try:
        for i in sorted(listdir(path)):
            name = join(path, i)
            if isfile(name):
                files_list.append((name, stat(name).st_size))
            else:
                print(i + " is not a file", file=stderr)
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
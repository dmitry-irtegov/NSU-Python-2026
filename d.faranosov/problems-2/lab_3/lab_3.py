from sys import argv, stderr
from os import listdir, stat
from os.path import isfile, join, isdir


def set_files(cor_path):

    if not(isdir(cor_path)):
        print("arg is not a path to a directory", file=stderr)
        exit(1)

    files = {}

    def set_files_in_dir(dir):
        files_in_dir = listdir(dir)
        for file in files_in_dir:
            file_path = join(dir, file)
            if isfile(file_path):
                info = stat(file_path)
                files[file_path] = info.st_size
            #elif isdir(file_path):
             #   set_files_in_dir(file_path)

    set_files_in_dir(cor_path)

    res_dict = sorted(files.items(), key=lambda item: (-item[1], item[0]))
    return res_dict

if __name__ == '__main__':
    if len(argv) < 2:
        print("No path to scan", file=stderr)
        exit(1)

    cor_path = argv[1]
    listed_files = set_files(cor_path)
    for (file, size) in listed_files:
        print(f'{file} -> {size} KB')




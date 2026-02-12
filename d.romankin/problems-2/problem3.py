from os import listdir, stat
from os.path import isfile, join
from sys import argv, stderr


path = argv[1]
files_list = []
for i in sorted(listdir(path)):
    name = join(path, i)
    if isfile(name):
        files_list.append((name, stat(name).st_size))
    else:
        print(i + " is not a file", file=stderr)

files_list = sorted(files_list, key=lambda file: -file[1])

for (name, size) in files_list:
    print(name, size)
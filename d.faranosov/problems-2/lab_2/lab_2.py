from sys import argv, stderr


def get_dict_from_file(file_path, encoding="utf-8"):
    res = dict()
    with open(file_path, 'r', encoding=encoding) as file:
        for line in file:
            line = line.replace(" ", "").replace("\n", "")
            left_right_sights = line.split(sep="-")
            if len(left_right_sights) != 2:
                print(f"wrong encoding: cnt of \"-\" is {len(left_right_sights)}", file=stderr)
                exit(1)
            key = left_right_sights[0]
            values = left_right_sights[1].split(",")
            if not(key.isalpha()):
                print(f"wrong encoding key is not a word key={key}", file=stderr)
            for value in values:
                if not(value.isalpha()):
                    print(f"wrong encoding, value is not a word, word={value}", file=stderr)
                    exit(1)

            res[key] = values
    return res

def convert_dict(file_dict):
    res = dict()
    for (key, values) in file_dict.items():
        for value in values:
            if value in res.keys():
                res[value].append(key)
            else:
                res[value] = [key]

    for key in res:
        res[key] = sorted(res[key])

    return sorted(res.items(), key=lambda x: x[0])

def convert_dict_from_file(file_path, encoding="utf-8"):
    file_dict = get_dict_from_file(file_path, encoding)
    return convert_dict(file_dict)


def write_dict(converted_list):
    for (key, values) in converted_list:
        print(f"{key} -> {values}\n")


if __name__ == '__main__':
    if len(argv) < 2:
        print("No file to convert\n[Usage]: python lab_2.py \"fileName\"", file=stderr)
        exit(1)
    file_path = argv[1]
    encoding="utf-8"
    if len(argv) > 2:
        encoding = argv[2]
    try:
        converted_dict = convert_dict_from_file(file_path, encoding)
        write_dict(converted_dict)

    except FileNotFoundError:
        print("Wrong file path", file=stderr)
        exit(1)
    except PermissionError:
        print("No rights for file", file=stderr)
        exit(1)
    except IsADirectoryError:
        print("file is not a regular", file=stderr)
        exit(1)
    except OSError as e:
        print(f"os error: {e}", file=stderr)
        exit(1)


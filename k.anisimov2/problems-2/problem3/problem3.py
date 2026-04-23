import sys
import os


def list_files_by_size(directory):
    if not isinstance(directory, str):
        raise TypeError("directory must be a string")
    if directory == "":
        raise ValueError("directory must not be empty")
    if not os.path.isdir(directory):
        raise ValueError(f"directory does not exist: {directory}")

    result = []

    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isfile(path):
            size = os.stat(path).st_size
            result.append((name, size))

    result.sort(key=lambda item: (-item[1], item[0]))
    return result


def format_files(files):
    if not isinstance(files, list):
        raise TypeError("files must be a list")

    lines = []
    for item in files:
        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("each file entry must be a tuple (name, size)")
        name, size = item
        lines.append(f"{name} {size}")

    return "\n".join(lines)


def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError("usage: python problem3.py <directory>")

        directory = sys.argv[1]
        files = list_files_by_size(directory)
        text = format_files(files)

    except KeyboardInterrupt:
        print("Interrupted by user.", file=sys.stderr)
        return
    except Exception as e:
        print(f"Input error: {e}", file=sys.stderr)
        return

    if text != "":
        print(text)


if __name__ == "__main__":
    main()

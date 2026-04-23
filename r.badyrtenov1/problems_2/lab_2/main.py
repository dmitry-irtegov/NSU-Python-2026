from sys import stderr


def make_latin_dict(file_path):
    d = dict()
    with open(file_path, 'r') as file:
        for line in file:
            if " - " not in line:
                continue
            pair = line.strip().split(" - ")
            key = pair[0]
            words = pair[1].split(", ")
            for w in words:
                d[w] = d.get(w, []) + [key]
    return {w: sorted(d[w]) for w in sorted(d)}


if __name__ == "__main__":
    try:
        res = make_latin_dict(input("Enter dictionary path: "))
        for la, eng in res.items():
            print(f"{la} - {', '.join(eng)}")
    except KeyboardInterrupt:
        print("Shutting down...")
    except Exception as e:
        print(f"Exception in main(): {e}", file=stderr)

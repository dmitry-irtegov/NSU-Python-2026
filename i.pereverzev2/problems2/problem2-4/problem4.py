import sys
import os


def find_indices(text, seq):
    indices = []
    if not seq:
        return indices

    pos = text.find(seq)
    while pos != -1:
        indices.append(pos)
        pos = text.find(seq, pos + 1)
    return indices


def run_search():
    try:
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, "pi.txt")
        
        with open(file_path, "r", encoding="utf-8") as file:
            pi_digits = file.read().strip()

        while True:
            print("Enter sequence to search for.")
            seq = input("> ")
            if not seq:
                break

            res = find_indices(pi_digits, seq)
            print(f"Found {len(res)} results.")

            if res:
                out = " ".join(map(str, res[:5])) + (" ..." if len(res) > 5 else "")
                print(f"Positions: {out}")

    except (EOFError, KeyboardInterrupt):
        pass
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)


if __name__ == "__main__":
    run_search()
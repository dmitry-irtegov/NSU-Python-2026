import sys

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
        with open('pi.txt', 'r') as f:
            pi_digits = f.read().strip()

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

if __name__ == '__main__':
    run_search()
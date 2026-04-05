from typing import List, Any, Iterable, Tuple
from sys import stderr


class Combinations:
    def __init__(self, arr: Iterable[Any], n: int):
        if not arr:
            raise ValueError("arr must not be empty")
        if n <= 0:
            raise ValueError("n must be positive")

        self.arr: List[Any] = list(arr)
        self.n: int = n
        self.count: int = len(self.arr)

        self.indexes: List[int] = [0] * n
        self.cur: List[Any] = [self.arr[0]] * n

    def current(self) -> Tuple[Any, ...]:
        return tuple(self.cur)

    def next(self) -> bool:
        i = self.n - 1

        while i >= 0:
            if self.indexes[i] < self.count - 1:
                self.indexes[i] += 1
                self.cur[i] = self.arr[self.indexes[i]]
                return False
            self.indexes[i] = 0
            self.cur[i] = self.arr[0]
            i -= 1
        return True


def parse_value(s: str) -> Any:
    s = s.strip()
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        return int(s)
    return s


def main() -> None:
    while True:
        raw = input("Enter elements (space separated): ")
        if raw == "":
            print("Enter at least one symbol")
        else:
            break

    lst = [parse_value(x) for x in raw.split()]
    while True:
        try:
            n = int(input("Enter n ").strip())
            break
        except ValueError:
            print("Need number")
        except Exception as e:
            print(f"Unexpected error: {e}", file=stderr)
            raise

    c = Combinations(lst, n)
    print(c.current())
    while True:
        c.next()
        enter = input("->")

        if enter == "exit" or enter == "e":
            print("Done")
            break

        print(c.current())


if __name__ == "__main__":
    main()

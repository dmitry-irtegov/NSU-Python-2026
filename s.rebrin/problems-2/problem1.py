from math import sqrt, gcd

def pythagorean_triples(N: int) -> list[tuple[int,int,int]]:
    if N <= 0:
        raise ValueError("Number must be positive")
    return [(m**2 - n**2, 2*m*n, m**2 + n**2)
       for n in range(1,int(sqrt(N))+1)
       for m in range(n+1,int(sqrt(N-n**2))+1)
        if gcd(n,m) == 1 and (m-n)%2 == 1]

def run_test() -> None:
    N = 100

    triples = pythagorean_triples(N)

    for a, b, c in triples:

        assert a > 0 and b > 0 and c > 0, f"({a, b, c}) contains non positive value"

        assert a <= N and b <= N and c <= N, f"({a, b, c}) contains value more then N"

        assert a**2 + b**2 == c**2, f"({a, b, c}) are not pythagorean triple"

        assert gcd(a,b,c) == 1, f"({a, b, c}) are not primitive pythagorean triple"

    expected = []
    for a in range(1, N + 1):
        for b in range(a, N + 1):
            c = sqrt(a ** 2 + b ** 2)
            if c.is_integer() and c <= N and gcd(a, b, int(c)) == 1:
                expected.append((a, b, int(c)))

    for e in expected:
        assert any(set(e) == set(t) for t in triples), f"{e} not found!"

    print("All tests passed")

from sys import stderr, exit
def main() -> None:
    while True:
        try:
            a = int(input())
            break
        except ValueError:
            print("Need number")
        except Exception as e:
            print(f"Unexpected error: {e}", file=stderr)
            exit(1)

    print(pythagorean_triples(a))


from sys import argv

if __name__ == "__main__":
    if "test" in argv:
        run_test()
    else:
        main()
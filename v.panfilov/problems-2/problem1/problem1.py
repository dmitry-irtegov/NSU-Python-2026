from sys import stderr

def calculate(n: int):
    array = [(a, b, c) for a in range(1, n)
            for b in range(a, n)
            for c in range(b, n) if (a ** 2 + b ** 2) == c ** 2]
    return array


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Please enter number: "))
            print(calculate(n))
            exit(0)
        except ValueError as e:
            print(f"Error: please enter valid integer number:\n{e}", file=stderr)
        except TypeError as e:
             print(f"Error: please enter valid integer number:\n{e}", file=stderr)
        except KeyboardInterrupt as e:
            print(f"Keyboard interrupt:\n{e}", file=stderr)
            exit()
        except IOError:
            print("Some Error occurred. Please enter valid integer number.", file=stderr)
        except Exception:
            print("Unexpected Error occurred.", file=stderr)
            exit()

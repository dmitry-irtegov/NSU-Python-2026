#!/usr/bin/env python3


def cumulative_sum(numbers):
    """Calculate cumulative sum with 0 as the first element

    Args:
        numbers: list of numbers

    Returns:
        list with cumulative sums, starting with 0

    Examples:
        >>> cumulative_sum([1, 2, 3])
        [0, 1, 3, 6]
        >>> cumulative_sum([ ])
        [0]
        >>> cumulative_sum([2.0, 3.0])
        [0, 2.0, 5.0]
    """
    result = [0]

    for num in numbers:
        result.append(result[-1] + num)

    return result


def parse_numbers(text):
    """Parse a string of numbers into a list of floats

    Args:
        text: string containing numbers separated by spaces, commas, or brackets

    Returns:
        list of floats, or None if parsing fails

    Examples:
        >>> parse_numbers("[1, 2, 3]")
        [1.0, 2.0, 3.0]
        >>> parse_numbers("1, 2,    3  ")
        [1.0, 2.0, 3.0]
        >>> parse_numbers("1,,,,,511")
        [1.0, 511.0]
        >>> parse_numbers("1 2 3")
        [1.0, 2.0, 3.0]
        >>> parse_numbers(".5 3.0")
        [0.5, 3.0]
    """
    normalized = text.replace("[", " ").replace("]", " ").replace(",", " ").split()

    try:
        return [float(x) for x in normalized]
    except ValueError:
        return None


def main():
    try:
        if sys.stdin.isatty():
            # interactive mode
            while True:
                try:
                    text = input()
                except KeyboardInterrupt:
                    print("KeyboardInterrupt", file=sys.stderr)
                    continue
                except EOFError:
                    print("Closing program on EOF", file=sys.stderr)
                    break

                numbers = parse_numbers(text)
                if numbers is None:
                    print("Error in input", file=sys.stderr)
                    continue

                print(cumulative_sum(numbers))
        else:
            # piped mode
            try:
                text = input()
            except KeyboardInterrupt:                                    
                print("KeyboardInterrupt", file=sys.stderr)              
                return                                                   
            except EOFError:                                             
                print("No input provided", file=sys.stderr)              
                return

            numbers = parse_numbers(text)
            if numbers is None:
                print("Error in input", file=sys.stderr)
                return
            print(cumulative_sum(numbers))
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)


if __name__ == "__main__":
    import sys

    main()

#!/usr/bin/env python3

def cumulative_sum(numbers):
    """
    [1, 2, 3] -> [0, 1, 3, 6]
    """
    result = [0]

    for i in range(len(numbers)):
        result.append(numbers[i] + result[i])

    return result

def parse_numbers(text):
    """
    parse input str to list int
    "[1, 2, 3]"     ->  [1, 2, 3]
    "1, 2,    3  "  ->  [1, 2, 3]
    "1,,,,,511"     ->  [1, 511]
    "1 2 3"         ->  [1, 2, 3]
    """
    normalized = (
        text.replace("[", " ")
        .replace("]", " ")
        .replace(",", " ")
        .split()
    )
    
    try:
        return [int(x) for x in normalized]
    except ValueError as err:
        raise ValueError("Could not convert text to an int") from err

def main():
    try:
        numbers = parse_numbers(input())
    except ValueError as err:
        print(f"Error in input: {err}")
        return

    print(cumulative_sum(numbers))


if __name__ == "__main__":
    main()

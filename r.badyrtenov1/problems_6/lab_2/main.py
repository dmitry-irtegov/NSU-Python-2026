#!/usr/bin/env python3

from re import IGNORECASE, compile
from sys import stderr

URL_RE = compile(
    r'(?:https?://|www\.)'
    r'[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+'
    r'(?:/[A-Za-z0-9._/\-]*)?'
    r'(?=$|[\s<>)\]}.,!?;:"\'])',
    IGNORECASE
)


def find_urls(s):
    return [match.group(0) for match in URL_RE.finditer(s)]


if __name__ == "__main__":
    try:
        print(find_urls(input()))
    except KeyboardInterrupt:
        print("Shutting down...", file=stderr)
    except Exception as e:
        print(f"Exception in main(): {e}", file=stderr)

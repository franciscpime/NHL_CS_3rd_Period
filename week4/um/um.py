import re
import sys


def main():
    text = input("Text: ")
    print(count(text))


def count(text):
    # Find occurrences of "um" as a standalone word (case-insensitive)
    matches = re.findall(r"\bum\b", text, re.IGNORECASE)

    # Return how many were found
    return len(matches)


if __name__ == "__main__":
    main()

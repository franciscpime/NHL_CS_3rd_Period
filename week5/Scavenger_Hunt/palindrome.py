def main() -> None:

    s = input(" Write something: ")

    if is_palindrome:
        print("Nice")
    else:
        print("Bad")

def is_palindrome(s: str) -> bool:
    # your code here
    s.strip(" ")
    s.lower()
    if s == s[::-1]:
        return True
    elif s[0] == s[-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
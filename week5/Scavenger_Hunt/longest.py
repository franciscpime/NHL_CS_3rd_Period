def main() -> None:

    sentence = input("Write: ")

    print(longest_word(sentence))


def longest_word(sentence: str) -> str:
    # your code here
    words = sentence.split()
    bigger = ""
    
    for word in words:
        if len(word) >= len(bigger):
            bigger = word
    
    return bigger


if __name__ == "__main__":
    main()
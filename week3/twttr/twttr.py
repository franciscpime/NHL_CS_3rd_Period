def main():
    message = input("Input: ")
    print(f"Output: {shorten(message)}")
            

def shorten(word):
    vowels = "aeiouAEIOU"
    transformed = ""

    for c in word:
        if c not in vowels:
            transformed += c
        else:
            transformed += ""
        
    return transformed


if __name__ == "__main__":
    main()
def main():
    message = input("Input: ")
    print(f"Output: {shorten(message)}")
            

def shorten(word):
    vowels = "aeiouAEIOU"
    transformed = ""

    if word.isdigit():
        return "Just Letters!"
    elif word == " ":
        return "Write Something!" 

    for c in word:
        if c not in vowels:
            transformed += c
        

    return transformed


if __name__ == "__main__":
    main()
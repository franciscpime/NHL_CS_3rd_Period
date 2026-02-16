def main():
    message = input("Input: ")
    print("Output: ", shorten(message), sep="")



def shorten(word):
    vowels = "aeiouAEIOU"

    for c in word:
        if c not in vowels:
            print(c, end="")

print()


if __name__ == "__main__":
    main()
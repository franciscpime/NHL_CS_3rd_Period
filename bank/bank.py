def main():
    greeting = input("Greeting: ").lower()
    print(value(greeting))


def value(greeting):
    if greeting.strip() == "hello" or greeting == "hello there" or greeting == "hello, newman":
        return "$0"
    elif greeting[0] == "h":
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()
import math

def main():
    while True:
        number = input("Write a number: ")
        print(factorize(number))


def factorize(number: str):

    if not number.isdigit():
        return "Dumb!"
    elif len(number) >= 4:
        return "Too much"
    else:
        return math.factorial(int(number))


if __name__ == "__main__":
    main()
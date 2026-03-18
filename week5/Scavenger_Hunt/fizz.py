def main() -> None:

    n = int(input("Write a number: "))

    print(fizzbuzz(n))

def fizzbuzz(n: int) -> str:
    #your code here
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)
    

if __name__ == '__main__':
    main()
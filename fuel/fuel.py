def main():
    while True:
        try:
            fraction = input("Fraction: ")

            gauge(percentage)

            if percentage >= 99:
                print("F")
            elif percentage <= 1:
                print("E")
            else:
                print(f"{percentage}%")

            break

        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    x, z = fraction.split("/")

    n1 = int(x)
    n2 = int(z)

    # validação obrigatória
    if n1 < 0 or n2 <= 0 or n1 > n2:
        return "Error!"
    else:
        return n1 / n2
                

def gauge(percentage):
    percentage = round(convert() * 100)

    return percentage

if __name__ == "__main__":
    main()

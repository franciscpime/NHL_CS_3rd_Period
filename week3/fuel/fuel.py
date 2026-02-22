def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            result = gauge(percentage)
            print(result)
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x, z = fraction.split("/")

    n1 = int(x)
    n2 = int(z)

    if n2 == 0:
        raise ZeroDivisionError

    if n1 < 0 or n2 < 0 or n1 > n2:
        raise ValueError

    percentage = round((n1 / n2) * 100)
    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
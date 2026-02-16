while True:
    try:
        fraction = input("Fraction: ")

        x, z = fraction.split("/")

        n1 = int(x)
        n2 = int(z)

        # validação obrigatória
        if n1 < 0 or n2 <= 0 or n1 > n2:
            continue

        percent = round((n1 / n2) * 100)

        if percent >= 99:
            print("F")
        elif percent <= 1:
            print("E")
        else:
            print(f"{percent}%")

        break

    except (ValueError, ZeroDivisionError):
        pass
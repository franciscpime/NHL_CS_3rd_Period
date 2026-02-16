fraction = input("Fraction: ")

x, z = fraction.split("/")

n1 = int(x)
n2 = int(z)

try:
    result = n1 / n2
    final_result = result * 100
        
    if final_result >= 99:
        print("F")
    elif final_result <= 1:
        print("E")
    else:
        print(f"{final_result:.0f}%")

except ValueError:
    if not n1.isdigit() or not n2.isdigit():
        ValueError
    elif n1 < 0 or n2 < 0:
        ValueError
    elif n1 > n2:
        ValueError
except ZeroDivisionError:
    if n2 == 0:
        print(ZeroDivisionError)
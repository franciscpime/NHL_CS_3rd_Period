expression = input("Expression: ")

x, y, z = expression.split()

n1 = int(x)
n2 = int(z)

if y == "+":
    expression = n1 + n2
    print(f"{expression:.1f}")
elif y == "-":
    expression = n1 - n2
    print(f"{expression:.1f}")
elif y == "*":
    expression = n1 * n2
    print(f"{expression:.1f}")
elif y == "/":
    expression = n1 / n2
    print(f"{expression:.1f}")






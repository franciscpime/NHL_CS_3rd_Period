price = 50

while price > 0:
    print((f"Amount Due: {price}"))
    amount = int(input("Insert coin: "))

    if amount == 25:
        price -= 25
    elif amount == 10:
        price -= 10
    elif amount == 5:
        price -= 5


change = abs(price)
print(f"Change Owed: {change}")

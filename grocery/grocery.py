groceries = {}

try:
    while True:
        item = input().upper()

        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1

except EOFError:
    pass

for item in sorted(groceries):
    print(groceries[item], item)
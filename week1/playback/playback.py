string = input("Message: ")
transformed = ""

for i in range(len(string)):
    if string[i] == " ":
        transformed += "..."
    else:
        transformed += string[i]

print(transformed)

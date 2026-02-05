variable = input("camelCase: ")
        
for c in variable:
    if c.isupper():
        print("_" + c.lower(), end="")
    else:
        print(c, end="")
    
print()

greeting = input("Greeting: ").lower()

if greeting.strip() == "hello" or greeting == "hello there" or greeting == "hello, newman":
    print("$0")
elif greeting[0] == "h":
    print("$20")
else:
    print("$100")
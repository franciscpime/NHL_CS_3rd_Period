def main():
    print()
    print("Welcome to the Survival Simulator!")
    print("You are in an abandoned supermarket and must solve puzzles to escape!")
    print()

    menu()


def menu():
    print("Choose an option:")
    print("1. File Extensions: What's in this file?")
    print("2. Math Interpreter: Unlock the safe")
    print("3. Nutrition Facts: Prepare a meal")
    print("4. CamelCase Decoder: Decode the message")
    print("5. Emojize: Guess the clue")
    print("6. Guessing Game: Guess the secret code")
    print("7. Exit")
    print()

    choice = input("Make a choice (1-7): ")

    if choice == "1":
        extension()
    elif choice == "2":
        math()
    elif choice == "3":
        meal()
    elif choice == "4":
        coke()
    elif choice == "5":
        camelCase()
    elif choice == "6":
        outdated()
    elif choice == "7":
        guessing()
    elif choice == "8":
        bitcoin()
    elif choice == "9":
        emojize()
    elif choice == "10":
        felipe()
    elif choice == "11":
        return


def extension():
    print("You find a file named 'recipe.pdf'.")
    
    file = input("Type the name of the file to check its extension: ")

    if file == "recipe.pdf":
        print("This is a PDF file containing a recipe!")
    else:
        print("Unknown file type!")
    
    menu()


def math():
    print("A safe unlocks only with the correct mathematical calculation.")

    while True:
        expression = input("Enter the mathematical expression: ")

        allowed = "0123456789+-*/"

        if any(c not in allowed for c in expression):
            print("Invalid characters!")
            continue

        try:
            result = eval(expression)

            if result == 14:
                print(f"The result is: {result}. The safe opens!")
                break
            else:
                print(f"{result} is incorrect... the safe remains locked.")

        except:
            print("That is not a valid mathematical expression!")
    
    menu()


def meal():
    print()
    print("You need to prepare a meal with 500 calories to proceed.")
    print("Available options: apple, banana, cookie, sandwich, water")
    print()

    total_choice = 0

    foods = {
        "apple" : "95",
        "banana" : "200",
        "cookie" : "350",
        "water" : "450",
        "sandwich" : "600"
    }    

    while total_choice <= 3:
        food = input("Choose an item to add to your meal: ")

        if food in foods:
            print(f"{food.title()} added! Total calories: {foods[food]}")
            total_choice += 1
        else: return

    print("Congratulations! Your meal is complete, and you have enough energy.")
    print()
    menu()


# def coke():



def camelCase():
    print()
    print("You find a message in CamelCase: 'EscapeNowThroughDoor'.")
    message = input("Type the CamelCase message to decode it: ")

    transformed = ""

    for c in message:
        if c.isupper():
            transformed += " "
            transformed += c
        else:
            transformed += c

    print(f"Decoded message: {transformed}")
    print()
    menu()


# def outdated():




# def guessing():





# def bitcoin():





def emojize():
    print()
    print("You find a clue in emojis: 🍎 🍌 🍪")

    emoji = input("What do these emojis mean? (Hint: food): ")

    a, b, c = emoji.split()

    if a == "apple" and b == "banana" and c == "cookie":
        print("Correct! You receive a key.")
    else:
        print("Wrong! try again.")

# def felipe():









main()
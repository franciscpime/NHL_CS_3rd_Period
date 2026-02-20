import random

progress = {
    "extension": False,
    "math": False,
    "meal": False,
    "coke": False,
    "camel": False,
    "outdated": False,
    "guessing": False,
    "bitcoin": False,
    "emojize": False,
    "felipe": False
}

WIDTH = 60

def line():
    print("═" * WIDTH)


def title(text):
    line()
    print(text.center(WIDTH))
    line()


def progress_bar(completed, total):
    percent = completed / total
    bars = int(percent * 30)
    bar = "🍱" * bars + "-" * (30 - bars)
    print(f"Progress: [{bar}] {completed}/{total}".center(WIDTH))


def pause():
    input("\nPress Enter to continue...")


def main():
    title("SURVIVAL SUPERMARKET SIMULATOR")
    print()
    print("Escape by completing all challenges!".center(WIDTH))
    print()
    menu()


def menu():
    while True:
        completed = sum(progress.values())
        total = len(progress)

        title("MAIN MENU")
        progress_bar(completed, total)
        print()

        options = [
            "1   │ File Extensions",
            "2   │ Math Interpreter",
            "3   │ Nutrition Facts",
            "4   │ Coke Machine",
            "5   │ CamelCase Decoder",
            "6   │ Outdated Products",
            "7   │ Guessing Game",
            "8   │ Bitcoin Investment",
            "9   │ Emojize",
            "10  │ Felipe's Taqueria",
            "11  │ Exit"
        ]

        print("=" * WIDTH)
        for option in options:
            print("  " + option)
        print("=" * WIDTH)

        choice = input("\nSelect option (1-11): ")

        if choice == "1":
            extension()
        elif choice == "2":
            math_game()
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
            completed = sum(progress.values())
            total = len(progress)

            if completed == total:
                title("ESCAPE SUCCESSFUL")
                print("YOU COMPLETED ALL CHALLENGES!".center(WIDTH))
                print("🎉 CONGRATULATIONS! 🎉".center(WIDTH))
                print("You escaped the supermarket.".center(WIDTH))
            else:
                title("GAME OVER")
                print("You tried to escape too early.".center(WIDTH))
                print(f"You completed {completed}/{total} challenges.".center(WIDTH))
                print("You lost.".center(WIDTH))
            break


def extension():
    title("FILE EXTENSIONS")
    file = input("Enter file name: ")
    print()

    if file.lower().endswith(".pdf"):
        print("PDF file detected. Recipe unlocked!".center(WIDTH))
        progress["extension"] = True
    else:
        print("Unknown file type.".center(WIDTH))

    pause()


def math_game():
    title("MATH INTERPRETER")
    print("Safe unlocks if result equals 14\n".center(WIDTH))

    while True:
        expression = input("Expression: ")
        allowed = "0123456789+-*/ "

        if any(c not in allowed for c in expression):
            print("Invalid characters!".center(WIDTH))
            continue

        try:
            result = eval(expression)
            if result == 14:
                print("Correct! Safe opened.".center(WIDTH))
                progress["math"] = True
                break
            else:
                print("Wrong result.".center(WIDTH))
        except:
            print("Invalid expression!".center(WIDTH))

    pause()


def meal():
    title("NUTRITION TABLE")

    foods = {
        "apple": 95,
        "banana": 105,
        "cookie": 200,
        "sandwich": 300,
        "water": 0
    }

    print("Food".ljust(20) + "Calories".rjust(10))
    print("-" * 30)
    for f, c in foods.items():
        print(f.ljust(20) + str(c).rjust(10))

    print("\nTarget: 500 calories\n")
    total = 0

    while total < 500:
        food = input("Choose food: ").lower()

        if food in foods:
            total += foods[food]
            print(f"Total: {total}".center(WIDTH))
        else:
            print("Invalid food.".center(WIDTH))

        if total > 500:
            print("Too many calories!".center(WIDTH))
            pause()
            return

    print("Perfect balance achieved!".center(WIDTH))
    progress["meal"] = True
    pause()


def coke():
    title("COKE MACHINE")
    price = 50

    while price > 0:
        print(f"Amount Due: {price}".center(WIDTH))
        try:
            amount = int(input("Insert coin (5/10/25): "))
        except:
            continue

        if amount in [5, 10, 25]:
            price -= amount

    change = abs(price)
    print(f"Change Owed: {change}".center(WIDTH))
    progress["coke"] = True
    pause()


def camelCase():
    title("CAMELCASE DECODER")
    message = input("Enter message: ")

    transformed = ""
    for i, c in enumerate(message):
        if c.isupper() and i != 0:
            transformed += " " + c
        else:
            transformed += c

    print("\nDecoded:".center(WIDTH))
    print(transformed.center(WIDTH))
    progress["camel"] = True
    pause()


def outdated():
    title("OUTDATED PRODUCTS")

    items = ["Milk", "Apple", "Lettuce", "Bread", "Yogurt", "Meat",
             "Fish", "Cereals", "Tomato", "Banana", "Cheese"]

    print(", ".join(items))
    print("\nDairy products are expired.\n")

    expired = {"Milk", "Yogurt", "Cheese"}
    answer = input("Expired items (comma separated): ")

    user_set = set(item.strip().title() for item in answer.split(","))

    if user_set == expired:
        print("Correct!".center(WIDTH))
        progress["outdated"] = True
    else:
        print("Not correct.".center(WIDTH))

    pause()


def guessing():
    title("GUESSING GAME")

    answer = 7
    attempts = 3

    for i in range(attempts):
        try:
            guess = int(input(f"Attempt {i+1}/3: "))
        except:
            continue

        if guess < answer:
            print("Too low!".center(WIDTH))
        elif guess > answer:
            print("Too high!".center(WIDTH))
        else:
            print("Correct!".center(WIDTH))
            progress["guessing"] = True
            pause()
            return

    print("You failed.".center(WIDTH))
    pause()


def bitcoin():
    title("BITCOIN INVESTMENT")

    price = random.randint(20000, 60000)
    print(f"Current price: ${price}\n".center(WIDTH))

    decision = input("Buy? (yes/no): ").lower()
    future = price + random.randint(-10000, 15000)

    print(f"\nLater price: ${future}".center(WIDTH))

    if decision == "yes":
        if future > price:
            print("Profit!".center(WIDTH))
        else:
            print("You lost money.".center(WIDTH))
    else:
        print("No investment made.".center(WIDTH))

    progress["bitcoin"] = True
    pause()


def emojize():
    title("EMOJIZE")

    print("Clue: 🧠 🦓 🦁\n")
    print("The word formed is a COUNTRY.\n")

    attempts = 0

    while True:
        answer = input("Country: ").lower().strip()
        attempts += 1

        if answer == "brazil":
            print("Correct!".center(WIDTH))
            progress["emojize"] = True
            pause()
            return

        if attempts == 1:
            print("\nHint: It is in South America.".center(WIDTH))
        elif attempts == 2:
            print("\nHint: It starts with 'B' and has 6 letters.".center(WIDTH))
        else:
            print("\nWrong.".center(WIDTH))


def felipe():
    title("FELIPE'S TAQUERIA")

    ingredients = ["tortilla", "beef", "chicken",
                   "cheese", "lettuce", "tomato"]

    print("Available ingredients:\n")
    print(", ".join(ingredients))
    print()

    while True:
        item = input("Add ingredient (or done): ").lower()

        if item == "done":
            break

        if item in ingredients:
            print(f"{item} added.".center(WIDTH))
        else:
            print("Not available.".center(WIDTH))

    print("\nYour taco is ready!".center(WIDTH))
    progress["felipe"] = True
    pause()


main()
def main(): 
    welcome_message()  

    total = 0  

    while True: 
        order = input("Please enter your order or type 'done' to finish: ") 

        if order.lower() == "done":  
            break 

        show_order(order)  
        energy_calculation() 
        total += get_price() 

    print(f"Your total is ${total:.2f}.")  

    tip_calculation(total)  
    print("Thank you for visiting Smart Café!")  


def welcome_message(): 
    print("Welcome to Smart Café!") 
    answer = input("Would you like to customize the welcome message? (yes/no): ").lower()  
    
    if answer == "yes": 
        message = input("Enter your custom message: ")  
        transformed = "" 

        for i in range(len(message)):                       # Loop through each character
            transformed += message[i]                       # Add character
            if i != len(message) - 1:                       # Avoid adding dots at the end
                transformed += "..."                        # Add dots between characters

        print(f"Transformed welcome message: {transformed}")    


def show_order(order):  
    # Dictionary of keywords and emojis
    emojis = { 
        "coffee": "☕️",
        "tea": "🍵",
        "cake": "🍰",
        "cookie": "🍪",
        "sushi": "🍱"
    }

    order_lower = order.lower()  

    if order_lower in emojis:  
        print(f"Okay, I will prepare {order_lower} {emojis[order_lower]}")  
    else:
        print(f"Okay, I will prepare {order_lower}")  


def energy_calculation():  
    answer = input("Would you like to calculate energy? (yes/no): ").lower()  

    if answer == "yes":  
        weight = float(input("Enter the weight in grams: "))  

        mass = weight / 1000                             # Convert grams to kilograms
        c = 299792458                                    # Speed of light
        energy = mass * pow(c, 2)                        # Calculate energy using E = mc^2

        print(f"Energy: {energy:.2e} Joules.")  


def get_price():  
    price = float(input("Enter the price of this item: $"))  
    return price  


def tip_calculation(total):  
    tip = int(input("How much tip would you like to add? (10, 15, 20): "))  

    final_total = total + (total * tip / 100)  

    print(f"With tip, your total is: ${final_total:.2f}")  


main()

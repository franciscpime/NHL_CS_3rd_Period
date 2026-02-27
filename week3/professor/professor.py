import random

def main():
    level = get_level()

    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        tries = 0
        answer = x + y

        while tries < 3:
            try:
                operation = int(input(f"{x} + {y} = "))

                if operation == answer:
                    score +=1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1
                
        if tries == 3:
            print(f"{x} + {y} = {answer}")
               
    print(score)

    
def get_level():
    while True:
        try:
            level = input("Level: ")

            right = "123"

            if level not in right:
                continue
            else:
                break
                
        except ValueError:
            pass

    return level
    
def generate_integer(level):

    level = int(level)
    
    if level == 1:
        number = random.randint(0, 9)
    elif level == 2:
        number = random.randint(10, 99)
    elif level == 3:
        number = random.randint(100, 999)

    return number


if __name__ == "__main__":
    main()
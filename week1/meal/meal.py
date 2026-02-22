def main():
    time = input("What time is it? ")
    hours = convert(time)

    if 7.0 <= hours <= 8.0:
        print("Breakfast time")
    elif 12.0 <= hours <= 13.0:
        print("Lunch time")
    elif 18.0 <= hours <= 19.0:
        print("Dinner time")


def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60


if __name__ == "__main__":
    main()

import re

def main():
    user_input = input("Hours: ")
    print(convert(user_input))


def convert(time_range):
    # Match formats like:
    # 9 AM to 5 PM
    # 9:30 AM to 5:45 PM
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.search(pattern, time_range)

    # If the format doesn't match, raise an error
    if not match:
        raise ValueError

    # Extract captured groups
    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    start_hour = int(start_hour)
    end_hour = int(end_hour)

    # If minutes are missing, assume 00
    start_minute = int(start_minute) if start_minute else 0
    end_minute = int(end_minute) if end_minute else 0

    # Validate time values
    if start_hour > 12 or end_hour > 12:
        raise ValueError
    if start_minute >= 60 or end_minute >= 60:
        raise ValueError

    # Convert start time to 24-hour format
    if start_period == "PM" and start_hour != 12:
        start_hour += 12
    if start_period == "AM" and start_hour == 12:
        start_hour = 0

    # Convert end time to 24-hour format
    if end_period == "PM" and end_hour != 12:
        end_hour += 12
    if end_period == "AM" and end_hour == 12:
        end_hour = 0

    return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"


if __name__ == "__main__":
    main()

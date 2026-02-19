months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    try:
        date = input("Date: ").strip()

        # formato numérico
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

        # formato textual
        else:
            month, day, year = date.split()

            # TEM de ter vírgula
            if not day.endswith(","):
                continue

            day = day.replace(",", "")

            month = months[month]
            day = int(day)
            year = int(year)

        # validações
        if not (1 <= month <= 12 and 1 <= day <= 31):
            continue

        print(f"{year:04}-{month:02}-{day:02}")
        break

    except (ValueError, KeyError):
        continue
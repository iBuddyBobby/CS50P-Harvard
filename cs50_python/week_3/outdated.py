months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()
    x = date.split("/")

    if len(x) == 3:
        try:
            month, day, year = map(int, x)
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04d}-{month:02d}-{day:02d}")
                break
        except ValueError:
            pass
    else:
        x = date.split(",")
        if len(x) == 2:
            try:
                month, day = x[0].split()
                month = months.index(month) + 1
                day, year = int(day), int(x[1])
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break
            except (ValueError, IndexError):
                pass


def main():
    time = input("What time is it? ").strip()
    time_as_float = convert(time)

    if 7 <= time_as_float < 11.5:
        print("breakfast time")
    elif 11.5 <= time_as_float < 15:
        print("lunch time")
    elif 15 <= time_as_float < 20:
        print("dinner time")


def convert(time: str) -> float:
    hours, minutes = map(int, time.split(":"))
    return hours + minutes / 60


if __name__ == "__main__":
    main()

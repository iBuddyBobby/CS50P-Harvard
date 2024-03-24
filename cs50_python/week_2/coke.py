change_owned = 50

while change_owned > 0:
    print(f"Amount Due: {change_owned}")

    coin = int(input("Insert coin: "))

    if coin in [50, 25, 10, 5]:
        change_owned -= coin

    print(f"Change Owed: {abs(change_owned)}")


while True:
    try:
        x, y = map(int, input("Fraction: ").split("/"))
        if y < x:
            raise ValueError
        elif y == 0:
            raise ZeroDivisionError
        percent = (x / y) * 100
        if percent <= 1:
            print('E')
        elif percent >= 99:
            print('F')
        else:
            print(f'{percent:.0f}%')
        break
    except ValueError as ve:
        print(f"Error: {ve}")
    except ZeroDivisionError as ze:
        print(f"Error: {ze}")

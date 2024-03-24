import random

max_attempts = 3
max_que = 10

def main():
    user_level = get_level()
    points = 0

    for _ in range(max_que):
        num1, num2 = gen_int(user_level)
        attempts = 0

        while attempts < max_attempts:
            try:
                ans = int(input(f"{num1} + {num2} = ".strip()))
                if ans == num1 + num2:
                    points += 1
                    break
                else:
                    attempts += 1
                    print("EEE")
            except ValueError:
                continue

        print(f"Answer: {num1} + {num2} = {num1 + num2}")

    print("Points: ", points)

def get_level() -> int:  # to select level
    while True:
        try:
            level = int(input("Level: ".strip()).strip())
            if level in [1, 2, 3]:
                return level
        except ValueError:
            continue

def gen_int(level):  # for generating random arthematic math equ at diff levels
    if level == 1:
        return random.randint(0, 9), random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99), random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999), random.randint(100, 999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()

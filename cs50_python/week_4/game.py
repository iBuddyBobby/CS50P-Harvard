import random


while True:
    try:
        level = int(input("Level: "))
        if level >= 1:
            break
    except ValueError:
        pass


random_number = random.randint(1, level)


while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            pass
            continue

        if guess > random_number:
            print("Too large!")
        elif guess < random_number:
            print("Too small!")
        else:
            print("Just right!")
            break
    except ValueError:
        print("")

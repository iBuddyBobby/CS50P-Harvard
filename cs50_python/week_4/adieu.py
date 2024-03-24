import inflect

p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ".strip())
    except EOFError:
        print()
        break
    else:
        if name:
            names.append(name)
        else:
            print("")

if names:
    print(f"Adieu, adieu, to {p.join(names)}")
else:
    print()

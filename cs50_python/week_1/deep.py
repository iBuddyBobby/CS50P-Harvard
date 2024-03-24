ask = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
x = ask.lower().strip()

if x == "42" or x == "forty-two" or x == "forty two":
    print("yes")

else:
    print("No")

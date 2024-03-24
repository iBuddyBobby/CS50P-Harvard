text = input("Input: ")
vowels = ["a", "e", "i", "o", "u"]
output = ""

for c in text:
    if c.casefold() not in vowels:
        output += c

print("Output: ", output)

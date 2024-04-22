def main():
    word = input("Input: ")
    shorten = remove_vowels(word)
    print("Output: ", shorten)

def remove_vowels(word):
    vowels = ("aeiouAEIOU")
    return "".join(char for char in word if char not in vowels)

if __name__ == "__main__":
    main()

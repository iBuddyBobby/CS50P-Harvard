def main():
    plate = input("Plates: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) > 6 or len(s) < 2:
        return False


    if not s.isalnum():
        return False    

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    no_in_index = next((i for i, char in enumerate(s) if char.isdigit()), len(s))

    if no_in_index < len(s) and s[no_in_index] == '0':
        return False

    if any(char.isalpha() for char in s[no_in_index:]):
        return False


    return True


main()

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s.isalnum() or not 2 <= len(s) <= 6:
        return False

    if not s[:2].isalpha() or s[0] == '0' or s[-1].isdigit():
        return False

    num_positions = [i for i, c in enumerate(s) if c.isdigit()]
    if num_positions and (num_positions[0] != 0 or num_positions[-1] != len(s) - 1):
        return False

    return True

if __name__ == "__main__":
    main()

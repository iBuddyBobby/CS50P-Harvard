def camel_to_snake(camelCase):
    snake_case = ""
    for char in camelCase:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case.lstrip("_")

def main():
    camel_case_var = input("camelCase: ")
    snake_case_var = camel_to_snake(camel_case_var)
    print("snake_case: ", snake_case_var)

if __name__ == "__main__":
    main()

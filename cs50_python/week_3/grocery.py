def main():
    grocery = {}
    try:
        while True:
            try:
                item = input("".strip().lower())
            except EOFError:
                break
            grocery[item] = grocery.get(item, 0) + 1
    except KeyboardInterrupt:
        pass

    x = sorted(grocery.items(), key=lambda x: x[0])
    for item, count in x:
        print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()

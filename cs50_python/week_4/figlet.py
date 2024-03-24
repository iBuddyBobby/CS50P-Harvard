from pyfiglet import Figlet
import sys

def main():
    figlet = Figlet()

    if len(sys.argv) == 1:
        text = input("Input: ")
    elif len(sys.argv) == 3 and sys.argv[1] in ('-f', '--font'):
        font_name = sys.argv[2]
        if font_name in figlet.getFonts():
            figlet.setFont(font=font_name)
            text = input("Input: ")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    print(figlet.renderText(text))

if __name__ == "__main__":
    main()

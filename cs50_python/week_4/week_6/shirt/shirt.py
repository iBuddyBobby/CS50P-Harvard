import os
import sys
from PIL import Image, ImageOps


def main() -> None:                                #Muppet's dress upp begins.
    if len(sys.argv) != 3:
        print("Usage: python shirt.py <input> <output>", file=sys.stderr)
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    if not os.path.isfile(input_path):
        print(f"Invalid input - {input_path}", file=sys.stderr)
        sys.exit(1)

    if not format_check(input_path) or not format_check(output_path):
        print("Invalid input", file=sys.stderr)
        sys.exit(1)

    if not format_same(input_path, output_path):
        print("Input and output have different extensions", file=sys.stderr)
        sys.exit(1)

    fit_shirt(input_path, output_path)


def format_check(input_filetype):                        #Check if the input is a valid format
    valid_formats = set(["jpg", "jpeg", "png"])
    return input_filetype.split(".", maxsplit=1)[1] in valid_formats


def format_same(input_file, output_file):
    _, fn_ext = input_file.split(".", maxsplit=1)

    if output_file.endswith(fn_ext):
        return True
    else:
        return False


def fit_shirt(input_file, output_file):
    shirt = Image.open("shirt.png")
    photo = Image.open(input_file)

    a, b = shirt.size
    photo = ImageOps.fit(photo, (a, b))
    #Pastes the shirt on the image
    photo.paste(shirt, shirt)
    photo.save(output_file)


if __name__ == "__main__":
    main()

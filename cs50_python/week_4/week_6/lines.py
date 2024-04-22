import sys

def cmd_check() -> None:
    if len(sys.argv) < 2:
        sys.exit("Too few cmd line args")
    if len(sys.argv) > 2:
        sys.exit("Too many cmd line args")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")
def is_valid(line: str) -> bool:
    return not line.strip() or line.lstrip().startswith("#")

cmd_check()
try:
    file = open(sys.argv[1], "r") # opens and reads the file
    lines = file.readlines()
except FileNotFoundError:
    sys.exit("File does not exist")

cnt = 0
for line in lines:
    if not is_valid(line):
        cnt += 1
print(cnt)

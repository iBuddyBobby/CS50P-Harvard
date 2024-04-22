import sys
import csv
from tabulate import tabulate
# +--------------+--------+--------+
# | Sicilian Pizza| Small | Large |
# +--------------+--------+--------+
# | Cheese       | $25.50| $39.95|
# | 1 item      | $27.50| $41.95|
# | 2 items     | $29.50| $43.95|
# | 3 items     | $31.50| $45.95|
# | Special      | $33.50| $47.95|
# +--------------+--------+--------+

if len(sys.argv) != 2:
    sys.exit("Expected one command-line argument")

csv_file = sys.argv[1]
if not csv_file.endswith(".csv"):
    sys.exit("Not a CSV file")

with open(csv_file, "r") as file:
    reader = csv.reader(file)
    headers = next(reader)
    table = list(map(tuple, reader))

print(tabulate(table, headers, tablefmt="grid"))

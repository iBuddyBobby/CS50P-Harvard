import sys
import csv

if len(sys.argv) != 3:
    sys.exit("Usage: python scourgify.py input.csv output.csv")

inp = sys.argv[1] #.............................................setting the I/O file
out = sys.argv[2]
data = []

with open(inp) as file: #.......................................filters the data according to F_name, L_name and House
    rows = csv.DictReader(file)
    for row in rows:
        l_name, f_name = row["name"].split(",")
        data.append({
            "first": f_name.strip(),
            "last": l_name.strip(),
            "house": row["house"]
        })

with open(out, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    writer.writerows(data)

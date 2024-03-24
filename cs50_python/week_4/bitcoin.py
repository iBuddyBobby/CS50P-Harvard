import sys
import requests

if len(sys.argv) != 2:
    sys.exit(1)

try:
    n = float(sys.argv[1].rstrip())
except ValueError:
    sys.exit(1)

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    rate = float(response.json()["bpi"]["USD"]["rate_float"])
    amount = rate * n
    print(f"${amount:,.4f}")
except requests.RequestException:
    pass

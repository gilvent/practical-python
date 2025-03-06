# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename, "rt") as file:
        rows = csv.reader(file)
        next(rows)
        for row in rows:
            holding = {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            portfolio.append(holding)
    return portfolio


def read_prices(filename):
    prices = {}
    issue_count = 0
    with open(filename, "rt") as file:
        rows = csv.reader(file)

        for index, row in enumerate(rows):
            try:
                prices[row[0]] = float(row[1])
            except:
                print(f"Found issue in row {index + 1} when reading {filename}")

    return prices


def make_report(portfolio, prices):
    report = []

    for stock in portfolio:
        buy_value = stock["shares"] * stock["price"]
        market_value = stock["shares"] * prices[stock["name"]]
        unrealized_value = market_value - buy_value
        status = (
            "GAIN" if unrealized_value > 0 else "LOSS" if unrealized_value < 0 else "-"
        )
        report.append(
            (
                stock["name"],
                stock["shares"],
                f"${stock["price"]:>0.2f}",
                buy_value,
                f"${prices[stock["name"]]:>0.2f}",
                market_value,
                unrealized_value,
                status,
            )
        )
    return report


portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")
report = make_report(portfolio, prices)

headers = "%16s %16s %16s %16s %16s %16s %16s %16s" % (
    "Name",
    "Shares",
    "Buy Price",
    "Buy value",
    "Market Price",
    "Market Value",
    "Unrealized",
    "Status",
)
divider = "----------------"
dividers = "%16s %16s %16s %16s %16s %16s %16s %16s" % (
    divider,
    divider,
    divider,
    divider,
    divider,
    divider,
    divider,
    divider,
)

print(headers)
print(dividers)
for r in report:
    print("%16s %16d %16s %16.2f %16s %16.2f %16.2f %16s" % r)

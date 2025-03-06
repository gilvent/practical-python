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

        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except:
                issue_count += 1

    print(f"Found {issue_count} rows with issue when reading {filename}")

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
                stock["price"],
                buy_value,
                prices[stock["name"]],
                market_value,
                unrealized_value,
                status
            )
        )
    return report


portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")
report = make_report(portfolio, prices)

for r in report:
    print(r)
# report.py
#
# Exercise 2.4
import csv
from collections import Counter

## Also read some tricks about zipping and typing
### https://dabeaz-course.github.io/practical-python/Notes/02_Working_with_data/07_Objects.html
def read_portfolio(filename):
    portfolio = []
    with open(filename, "rt") as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            holding = dict(zip(headers, row))
            holding["shares"] = int(holding["shares"])
            holding["price"] = float(holding["price"])
            portfolio.append(holding)
    return portfolio


def read_prices(filename):
    prices = {}

    with open(filename, "rt") as file:
        reader = csv.reader(file)

        for index, row in enumerate(reader, start=1):
            try:
                prices[row[0]] = float(row[1])
            except:
                print(f"Found issue in row {index} when reading {filename}")

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


# exercise 2.10 string formatting
def print_report():
    portfolio = read_portfolio("Data/portfoliodate.csv")
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


# Exercise 2.18 Tabulating with Counter
def combine_shares():

    portfolio1 = read_portfolio("Data/portfolio.csv")
    portfolio2 = read_portfolio("Data/portfolio2.csv")

    holdings1 = Counter()
    for p1 in portfolio1:
        holdings1[p1["name"]] += p1["shares"]

    holdings2 = Counter()
    for p2 in portfolio2:
        holdings2[p2["name"]] += p2["shares"]

    # Counter automatically adds value of the same key from different Counter
    return holdings1 + holdings2


# Exercise 2.21 List comprehension
def total_portfolio_cost(portfolio_file):
    portfolio = read_portfolio(portfolio_file)

    return sum([stock["shares"] * stock["price"] for stock in portfolio])


def filtered_portfolios(portfolio_file, cost_larger_than=10000):
    portfolio = read_portfolio(portfolio_file)

    return [s for s in portfolio if s["shares"] * s["price"] > cost_larger_than]


# portfolios_by_name('Data/portfolio.csv', {'MSFT'})
def portfolios_by_name(portfolio_file, names_filter):
    portfolio = read_portfolio(portfolio_file)

    return [s for s in portfolio if s["name"] in names_filter]


# Exercise 2.23 Set and Dictionary Comprehension
def owned_shares(portfolio_file):
    portfolio = read_portfolio(portfolio_file)

    # Make unique set of stock names in portfolio (Set comprehension)
    owned_stock_names = {s["name"] for s in portfolio}

    # Make dictionary from the stock names (Dictionary comprehension)
    owned_shares = {name: 0 for name in owned_stock_names}

    # Fill the shares
    for p in portfolio:
        owned_shares[p["name"]] += p["shares"]

    return owned_shares


# Filter prices that only appear in portfolio
def portfolio_prices(portfolio_file, prices_file):
    prices = read_prices(prices_file)
    portfolio = read_portfolio(portfolio_file)

    # Make unique set of stock names in portfolio (Set comprehension)
    owned_stock_names = {s["name"] for s in portfolio}

    return {name: prices[name] for name in owned_stock_names}

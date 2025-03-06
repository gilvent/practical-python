# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(path):
    with open(path, "rt") as file:
        reader = csv.reader(file)
        headers = next(reader)
        total_price = 0

        for index, row in enumerate(reader, start = 1):
            data = dict(zip(headers, row))
            print(data)
            try:
                shares = int(data['shares'])
                price = float(data['price'])
                total_price += shares * price
            except ValueError:
                print(f"Row {index}: Couldn't convert {str(row)}")
        return total_price


# Enable to run this command in terminal
# python3 pcost.py Data/missing.csv
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print(cost)

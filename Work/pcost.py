# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(path):
    with open(path, "rt") as file:
        rows = csv.reader(file)
        next(file)
        total_price = 0
        for index, row in enumerate(rows, start = 1):
            try:
                shares = int(row[1])
                price = float(row[2])
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

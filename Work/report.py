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
            holding = {
                'name': row[0],
                'share': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(holding)
    return portfolio

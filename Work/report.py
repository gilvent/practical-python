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

def read_prices(filename):
    prices = {}
    issue_count = 0
    with open(filename, 'rt') as file:
        rows = csv.reader(file)

        for row in rows:
            try:
                prices[row[0]] = row[1]
            except:
                issue_count += 1
    
    print(f'Found {issue_count} rows with issue')

    return prices
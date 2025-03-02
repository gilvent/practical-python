# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(path):
    with open(path, 'rt') as file:
        rows = csv.reader(file)
        next(file)
        total_price = 0
        for row in rows:
            try:
                shares = int(row[1])
                price = float(row[2])
                total_price += shares * price
            except ValueError:
                print(f'Price for {row[0]} cannot be calculated due to missing value')
        return total_price
    
if len(sys.argv) == 2:
    filename = sys.argv[1] 
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(cost)
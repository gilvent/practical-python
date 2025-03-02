# pcost.py
#
# Exercise 1.27
def portfolio_cost():
    with open('Data/portfolio.csv', 'rt') as file:
        next(file)
        total_price = 0

        for row in file:
            row_data = row.removesuffix('\n').split(',')
            shares = int(row_data[1])
            price = float(row_data[2])
            total_price += shares * price
        return total_price
    
cost = portfolio_cost()
print(cost)
# pcost.py
#
# Exercise 1.27
def portfolio_cost(path):
    with open(path, 'rt') as file:
        next(file)
        total_price = 0

        for row in file:
            row_data = row.removesuffix('\n').split(',')
            try:
                shares = int(row_data[1])
                price = float(row_data[2])
                total_price += shares * price
            except ValueError:
                print(f'Price for {row_data[0]} cannot be calculated due to missing value')
        return total_price
    
cost = portfolio_cost('Data/missing.csv')
print(cost)
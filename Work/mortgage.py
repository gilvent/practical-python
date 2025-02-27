# mortgage.py
#
# Exercise 1.7
def calculateMortgagePayment (principal, rate, montly_payment):
    total_payment = 0.0

    while (principal > 0):
        principal = principal * (1 + rate / 12) - montly_payment
        total_payment += montly_payment
    
    return round(total_payment, 2)


print('Total paid', calculateMortgagePayment(500000, 0.05, 2684.11))
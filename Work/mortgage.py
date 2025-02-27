# mortgage.py
#
# Exercise 1.8 Extra Payments

def calculateWithExtraPayment (principal, rate, monthly_payment, first_year_extra_payment):
    total_payment = 0.0
    month = 0

    while (principal > 0):
        month += 1
        payment = monthly_payment

        if (month <= 12):
            payment = monthly_payment + first_year_extra_payment

        principal = principal * (1 + rate / 12) - payment
        total_payment += payment
    
    return [round(total_payment, 2), month]

[total_payment, months_required] = calculateWithExtraPayment(500000.0, 0.05, 2684.11, 1000)
print(total_payment, months_required)
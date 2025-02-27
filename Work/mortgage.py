# mortgage.py
#
# Exercise 1.9 Extra Payments on Custom Period
def calculateWithExtraPayment(
    principal,
    rate,
    monthly_payment,
    extra_payment_start_month,
    extra_payment_end_month,
    extra_payment,
):
    total_payment = 0.0
    month = 0

    while principal > 0:
        month += 1
        payment = monthly_payment
        principal_to_pay = principal * (1 + rate / 12)

        # Add extra payment if any
        if month >= extra_payment_start_month and month <= extra_payment_end_month:
            payment = monthly_payment + extra_payment

        # Last payment
        if principal_to_pay <= payment:
            payment = principal_to_pay

        principal = principal_to_pay - payment
        total_payment += payment
        print(month, total_payment, principal)

    return [round(total_payment, 2), month]


[total_payment, months_required] = calculateWithExtraPayment(
    500000.0, 0.05, 2684.11, 61, 108, 1000
)

print("Total payment", total_payment)
print("Months", months_required)

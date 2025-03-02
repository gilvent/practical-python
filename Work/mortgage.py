# mortgage.py
#
# Exercise 1.9 Extra Payments on Custom Period
def mortgage_with_extra_payment(
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


def mortgage_info():
    principal = 500000.0
    rate = 0.05
    monthly_payment = 2684.11
    extra_payment_start_month = 61
    extra_payment_end_month = 108
    extra_payment = 1000

    [total_payment, months_required] = mortgage_with_extra_payment(
        principal,
        rate,
        monthly_payment,
        extra_payment_start_month,
        extra_payment_end_month,
        extra_payment,
    )

    return f"""
If you are taking a mortgage with {principal} principal, {rate} rate and {monthly_payment} monthly payment,
and you want to pay {extra_payment} more starting from month {extra_payment_start_month} to month {extra_payment_end_month}.

You will be paying {total_payment} in {months_required} months.
"""


print(mortgage_info())

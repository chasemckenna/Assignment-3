# Exercise 6: Bank Loan Repayment Simulator
# Simulate paying off a loan month by month.
 
def months_to_pay_off(balance, annual_rate, payment):
    """Return how many months it takes to pay off the loan."""
    monthly_rate = annual_rate / 100 / 12
    months = 0
 
    while balance > 0:
        interest = balance * monthly_rate
        balance = balance + interest - payment
        months = months + 1
 
    return months
 
 
loan = float(input("Loan amount: $"))
rate = float(input("Annual interest rate (%): "))
payment = float(input("Monthly payment: $"))
 
# Check that the payment is bigger than the first month's interest,
# otherwise the loan would never be paid off (infinite loop).
first_interest = loan * rate / 100 / 12
 
if payment <= first_interest:
    print("Your payment is too small to ever pay off this loan.")
else:
    months = months_to_pay_off(loan, rate, payment)
    print(f"It will take {months} months to pay off the loan.")
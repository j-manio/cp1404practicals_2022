
"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

print("Bonuses")

sales = float(input("Sales:$"))
while sales >= 0:

    if sales < 1000:
        under_sale = sales * 0.10
        print(f'Bonus {under_sale:.0f}') # Discount 10% if under
    if sales >= 1000:
        over_sale = sales * 0.15
        print(f'Bonus:${over_sale:.0f}') # Discount 15% if over

    sales = float(input("Sales:$"))



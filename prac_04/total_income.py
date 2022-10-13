"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for list_of_incomes over a given number of number_of_months."""
    list_of_incomes = []
    number_of_months = int(input("How many number_of_months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        list_of_incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    print_income_report(list_of_incomes, number_of_months, total)


def print_income_report(list_of_incomes, number_of_months, total):
    """ This will print the income report """
    for month in range(1, number_of_months + 1):
        income = list_of_incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()

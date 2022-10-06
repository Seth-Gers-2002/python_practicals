"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    month_number = int(input("How many months? "))

    for month in range(1, month_number + 1):
        income = float(input(f"Enter income for month, {month}: " ))
        incomes.append(income)
    print_report(incomes, month_number)


def print_report(incomes, month_number):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, month_number + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
#
# We need a list to store the incomes.
# How do you add values to a list?
# get a number of them into a [] list
# We need a counter variable (int) for the month number.
# Remember that list indexes start at 0, but we want to print from 1.
# start loop at value 1, use a get int for months
# How many loops will we need? What kind of loops?
# two, one for loop for income and another for loop for total income
# We need a cumulative total to update as we loop through the list to display the incomes.
#
# And lastly we need to format the output nicely, which we can use f-strings for.
#
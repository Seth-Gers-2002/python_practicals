"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main(score):
    if score < 0.00 or score > 100.00:
        message = "Invalid score"
    elif score >= 90.00:
        message = "Excellent"
    elif score >= 50.00:
        message = "Passable"
    else:
        message = "Bad"
    return message

main(float(input("Enter score: ")))


print(message)

mystery = random.randint(0, 100)


main(mystery)


print(message)

"""
Check if a generated score is valid
"""
import random


def main(score):
    """Give a score a rating """
    if score < 0.00 or score > 100.00:
        return "Invalid score"
    elif score >= 90.00:
        return "Excellent"
    elif score >= 50.00:
        return "Passable"
    else:
        return "Bad"


score = float(input("Enter score: "))
print(main(score))
score = random.randint(0, 100)
print(main(score))

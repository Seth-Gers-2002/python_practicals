"""
CP1404/CP5632 - Practical
"""
import random


def score_check(score):
    """Give a score a rating """
    if score < 0.00 or score > 100.00:
        return "Invalid score"
    elif score >= 90.00:
        return "Excellent"
    elif score >= 50.00:
        return "Passable"
    else:
        return "Bad"

def main(number):
    """"Generate random number"""
    for i in range(0, number, 1):
        score = random.randint(0, 100)
        print(score, "is" ,score_check(score))


main((int(input("how many? "))))
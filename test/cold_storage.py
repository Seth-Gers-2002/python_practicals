"""
CP1404/CP5632 - Practical
"""
import random


def score_check(score):
    if score < 0.00 or score > 100.00:
        return "Invalid score"
    elif score >= 90.00:
        return "Excellent"
    elif score >= 50.00:
        return "Passable"
    else:
        return "Bad"

def main(number):
    results = open("results.txt")
    for i in range(0, number, 1):
        score = random.randint(0, 100)
        data = (score, "is" ,score_check(score))
        results.writes(str(data))
    results.close
    return results


number = (int(input("how many? ")))
print(main(number))
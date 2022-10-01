"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# noinspection PyArgumentList
def menu(choice):
    while choice != "Q":
        if choice == "S":
            score = int(input("Input score: "))
            print(score_check(score))
        elif choice == "*":
            score = (int(input("Input score: ")))
            print("*" * score)
        elif choice == "O":
            print("TYPE S for score, TYPE P to print Q for Quit:, O for Options")
        else:
            print("TYPE S for score, TYPE P to print Q for Quit:, O for Options")

        choice = (input("Enter value (O for Options): ").upper())


def score_check(score):
    if score < 0.00 or score > 100.00:
        return "Invalid score"
    elif score >= 90.00:
        return "Excellent"
    elif score >= 50.00:
        return "Passable"
    else:
        return "Bad"


menu(input("Select option:").upper())

print(score_check(score))

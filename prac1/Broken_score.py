"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
if score < 0.00 or score > 100.00:
    print("Invalid score")
elif score >= 90.00:
    print("Excellent")
elif score >= 50.00:
    print("Passable")
else:
    print("Bad")

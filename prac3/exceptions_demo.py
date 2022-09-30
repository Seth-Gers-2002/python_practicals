"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the input number isn't a int (x,y,z,eight,one).
2. When will a ZeroDivisionError occur?
When an invaild equation is calulated (4/0) that makes the value nothing.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Either create a loop that keeps asking for a vaild demonitor.
or
hardcode the exception to print the 0
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Invaild input")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
"""
Line 1
"smallest possible number is 5, largest is 20"
Line 2
smallest is 3
largest is nine
the generated number will always be produced within a range
this range forces all the generated numbers to be an odd number
due to is staring at 3 and adds 2 a random amount of time that's not >10
Line 3
smallest is 2.5
largest is 5.5
generates a random float number between 2.5 - 5.5 and goes to the *10^-15 digit
Line 4
made a randomise 1 >= x <=100
"""

import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
print(random.randint(1, 100)) # line 4

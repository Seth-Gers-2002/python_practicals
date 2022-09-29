import random

print(random.randint(5, 20))  # line 1
# "smallest possible number is 5, largest is 20"
print(random.randrange(3, 10, 2))  # line 2
# smallest is 3
# largest is nine
# the generated number will always be produced within a range
# this range forces all the generated numbers to be an odd number
# due to is staring at 3 and adds 2 a random amount of time that's not >10
print(random.uniform(2.5, 5.5))  # line 3
# smallest is 2.5
# largest is 5.5
# generates a random float number between 2.5 - 5.5 and goes to the *10^-15 digit

print(random.randint(1, 100))

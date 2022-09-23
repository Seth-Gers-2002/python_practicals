"""
make a program that asks how many items a person is buying
ask for the price
add them together and add a 10% discount if over %100
"""

Total = 0  # Total = Total Value Of Item
NOI = int(input("number of items:"))  # NOI = Number Of Items
while NOI < 0:
    NOI = int(input("number of items:"))  # NOI = Number Of Items
for i in range(0, NOI, 1):
    VOI = float(input("item:"))  # VOI = Value Of Item
    Total = Total + VOI
if Total > 100:
    Total = Total * .90
    print(Total)
else:
    print(round(Total))

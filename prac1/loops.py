
# start
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# A: from 0-100 in tens

for i in range(0, 100, 10):
    print(i, end=' ')
print()

# B count from 20-1 in ones

for i in range(20, 0, -1):
    print(i, end=' ')
print()

# C: print a number of stars
stars = int(input("number of stars"))
for i in range(0, stars, 1):
    print("*", end=' ')
print()

# d staircase of stars
count = 1
for y in range(0, stars, 1):
    for x in range(0, count, 1):
        print("*", end=' ')
    print()
    count = count + 1

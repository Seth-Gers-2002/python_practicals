numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers)
numbers[0] = 10
print(numbers)
last_number = len(numbers) - 1
numbers[last_number] = 1
print(numbers)
print(numbers[2:])
if 9 in numbers:
    print("9 is in numbers")
else:
    print("not in numbers")

# numbers[0]
# print 3
# numbers[-1]
# print 2
# numbers[3]
# print 1
# numbers[:-1]
# print 314159
# numbers[3:4]
# 1
# 5 in numbers
#True
# 7 in numbers
# False
# "3" in numbers
# False
# numbers + [6, 5, 3]
# 3141592653
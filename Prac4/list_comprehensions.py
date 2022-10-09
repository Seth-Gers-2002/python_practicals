"""
CP1404/CP5632 Practical
List comprehensions
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# for loop that creates a new list containing the first letter of each name
first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

# list comprehension that does the same thing as the loop above
first_initials = [name[0] for name in names]
print(first_initials)

# list comprehension that creates a list containing the initials
# this splits each name and adds the first letters of each part to a string
full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(full_initials)

# this example uses filtering to select only the names that start with A
a_names = [name for name in names if name.startswith('A')]
print(a_names)

# and here's the join string method being used to create a single string from the names like:
# 'Ada Alan Angel Bob Jimi'
print(" ".join(sorted(names)))

lowercase_full_names = []
for name in full_names:
    lowercase = name.lower()
    lowercase_full_names.append(lowercase)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
numbers = []
for digit in almost_numbers:
    number = int(digit)
    numbers.append(number)

greater_numbers = []
for digit in numbers:
    if digit > 9:
        greater_numbers.append(digit)


text = "last names for those full names longer than 11 characters"

for name in full_names:
    first_last = name.split(" ")
    last_name = first_last[1]
    if len(name) > 11:
        text += ", " + last_name

print(text)
"""#1 Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
Remember to close your file. #2 Write code that opens "name.txt" and reads the name (as above) then prints,
"Your name is Bob" (or whatever the name is in the file). #3 Create a text file called numbers.txt and save it in
your prac directory. Put the following three numbers on separate lines in the file and save it: 17 42 400 Write code
that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result,
which should be... 59. #4 Now write a fourth block of code that prints the total for all lines in numbers.txt or a
file with any number of numbers.

read()
readline()
readlines()
for line in file
"""

#1
name = input("what is your name?")
add_to_name = open("name.txt", 'w')
print(f"{name}", file=add_to_name)
add_to_name.close()

#2
read_name = open("name.txt", 'r')
answer = read_name.readline()
print("Your name is", answer)
read_name.close()

# 3
file_numbers = open("numbers.txt", 'r')
find_number1 = int(file_numbers.readline())
find_number2 = int(file_numbers.readline())
file_numbers.close()
print(find_number1 + find_number2)

# 4
sum_of_file = 0
file_numbers = open("numbers.txt", 'r')
for line in file_numbers:
    sum_of_file += int(line)
file_numbers.close()
print(sum_of_file)

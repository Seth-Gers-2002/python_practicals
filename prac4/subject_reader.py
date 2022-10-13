"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print_information(data)


def print_information(list):
    for index in range(0, len(list)):
        print(f"{list[index][0]} is taught by, {list[index][1]} and has {list[index][2]}")


def get_data():
    stored = []
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:

        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        stored.append(parts)

    input_file.close()
    return stored

main()
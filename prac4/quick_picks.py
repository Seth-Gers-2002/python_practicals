import random

number_per_line = 6
min_value = 1
max_value = 45


def main():
    number_of_quick_picks = int(input("how many quick picks:"))
    while number_of_quick_picks < 0:
        number_of_quick_picks = int(input("invalid number, try again:"))

    for i in range(number_of_quick_picks):
        quick_picks = []
        for j in range(number_per_line):
            value = random.randint(min_value, max_value)
            while value in quick_picks:
                value = random.randint(min_value, max_value)
            quick_picks.append(value)
        quick_picks.sort()
        print(quick_picks)


main()

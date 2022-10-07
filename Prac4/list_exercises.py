print('please give me five numbers')


def main():
    get_numbers()
    print_numbers()
    numbers_sorted()


def numbers_sorted():
    organised = sorted(numbers)
    numbers_min = organised[0]
    numbers_max = organised[4]
    print(f"numbers_min:{numbers_min}, numbers_max{numbers_max}")
    average = sum(numbers) / 5
    print(average)


def print_numbers():
    print(numbers)
    numbers_first = numbers[0]
    numbers_last = numbers[4]
    print(f"first number:{numbers_first}, last number:{numbers_last}")


def get_numbers():
    for i in range(0, 5, 1):
        number = int(input("number"))
        numbers.append(number)


numbers = []
main()

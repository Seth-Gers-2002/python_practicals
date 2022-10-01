"""
convert Fahrenheit to Celsius and vice versa
"""
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def convert_to_fahrenheit(fahrenheit):
    """convert celsius to fahrenheit"""
    return (fahrenheit * 9.0 / 5) + 32


def convert_to_celsius(celsius):
    """convert fahrenheit to celsius"""
    return 5 / 9 * (celsius - 32)


while choice != "Q":
    if choice == "C":
        fahrenheit = float(input("Celsius: "))
        print("Result: {:.2f} F".format(convert_to_fahrenheit(fahrenheit)))
    elif choice == "F":
        celsius = float(input("Fahrenheit: "))
        print("Result: {:.2f} C".format(convert_to_celsius(celsius)))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")

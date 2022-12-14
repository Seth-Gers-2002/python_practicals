"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.

estimated time: 20 mins
actual time: 2 hours
"""

from prac6.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("my car", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    my_limo = Car("limo", 180)
    my_limo.add_fuel(20)
    print(f"limo has fuel:{my_limo.fuel}")
    my_limo.drive(115)
    print(my_limo)

main()
from prac9.taxi import Taxi


def main():
    my_car = Taxi("prius 1 ", 100)
    my_car.drive(40)
    print(my_car)
    my_car.start_fare()
    my_car.drive(100)
    print(my_car)


main()

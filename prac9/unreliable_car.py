from random import randint

from prac9.car import Car


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability=0.00):
        super().__init__(name, fuel)
        self.name = name
        self.fuel = fuel
        self.odometer = 0
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()}, {self.reliability}%"

    def drive(self, distance):
        ability = randint(0, 100)
        if ability <= self.reliability:
            return "you can drive"
        return "you cannot drive"

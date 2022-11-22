from prac9.taxi import Taxi


class SilverServiceTaxi(Taxi):

    flagfall = 4.5

    def __init__(self, name, fuel, fanciness=0.00):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.fanciness = fanciness
        self.price_per_km *= 1.23

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()}, plus flagfall of${self.flagfall:.}"

"""

"""
CURRENT_YEAR = 2017

class Guitar:

    def __init__(self, name="", year=0, cost=0):
        """Initialises Guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of Guitar"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Get the age of Guitar"""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Check if the Guitar is vintage"""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Less than, used for sorting Guitars - by year released."""
        return self.year < other.year


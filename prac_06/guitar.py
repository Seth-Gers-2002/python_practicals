"""

"""


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.age = None
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost},"

    def get_age(self):
        self.age = 2022 - self.year
        return self.age

    def is_vintage(self):
        if self.age >= 50:
            return True

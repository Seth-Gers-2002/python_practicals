"""

"""


class Guitar:

    def __init__(self, name=" ", year=0, cost=0):
        self.age = 2022
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost},"

    def get_age(self):
        age = self.age - self.year
        return age

    def is_vintage(self):
        if self.age >= 50:
            return True

"""
Guitar - Practical 06
Estimate: 90 min
Actual:
"""

CURRENT_YEAR = 2022
VINTAGE_YEAR = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year} : ${self.cost:.2f})"

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        if self.get_age() > VINTAGE_YEAR:
            return True

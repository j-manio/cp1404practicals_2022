"""
Unreliable Car
Cp1404 - Practical 9
"""
from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Unreliable car"""
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        random_integer = randint(1, 100)

        if random_integer >= self.reliability:
            distance = 0
        distance_drove = super().drive(distance)
        return distance_drove




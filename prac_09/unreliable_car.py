"""
Unreliable Car
Cp1404 - Practical 9
"""
from prac_09.car import Car


class UnreliableCar(Car):
    """Unreliable car"""
    def __init__(self, name, fuel, reliability):
        self.name = name
        self.fuel = fuel
        self.reliability = reliability


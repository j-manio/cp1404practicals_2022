"""
Silver Service Taxi
CP1404 - Practical 9
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Initiate Silver Service Tax"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness, price_per_km):
        super().__init__(name, fuel, price_per_km)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"



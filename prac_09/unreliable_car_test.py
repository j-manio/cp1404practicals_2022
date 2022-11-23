"""
Unreliable Car test
CP1404 - Practical 9
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    unreliable_used_car = UnreliableCar("Subaru WRX", 100, 50)
    reliable_new_car = UnreliableCar("Rav4", 100, 65)
    for i in range(1, 20):
        print(f"Attempting to drive {i}km:")
        print(f"{reliable_new_car.name:12} drove {reliable_new_car.drive(i):2}km")
        print(f"{unreliable_used_car.name:12} drove {unreliable_used_car.drive(i):2}km")

    print(unreliable_used_car)
    print(reliable_new_car)


main()

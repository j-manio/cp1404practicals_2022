"""
Taxi Simulator
CP1404 - Practical 9
"""

from prac_09.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_sevice_taxi import SilverServiceTaxi


MENU = """q)uit, c)hoose, d)rive
"""


def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4,)]

    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")

            # no error-checking
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif menu_choice == "d":
            pass
        else:
            print("Invalid option")
        print("Bill to date: ${total_bill:.2f}")
        print(MENU)
        menu_choice = input(">>> ").lower()








main()


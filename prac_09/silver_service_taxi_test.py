"""
Silver Service Taxi Test
CP1404 - Practical 9
"""
from prac_09.silver_sevice_taxi import SilverServiceTaxi


def main():
    """Test for Silver Service Taxi """
    tsv_silver_cabs = SilverServiceTaxi("Prius Taxi", 100, 2, 4.92)
    tsv_silver_cabs.drive(18)
    print(tsv_silver_cabs)
    print(tsv_silver_cabs.get_fare())


main()

from prac_06.guitar import Guitar


def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    another_guitar = Guitar("Another Guitar", 2013, 16035.40)
    print(f"My guitar: {guitar}, first made in {year}")

    print(f"{name} get_age() - Expected {guitar.get_age()}. Got {guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected {another_guitar.get_age()}. Got {another_guitar.get_age()} ")
    print(f"{name} is_vintage() - Expected {guitar.is_vintage()}. Got {guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected {another_guitar.is_vintage()}. "
          f"Got {another_guitar.is_vintage()}")
    print(f"50-year old guitar is_vintage() - Expected {guitar.is_vintage()}. Got {another_guitar.is_vintage()}")


main()

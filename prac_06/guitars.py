from prac_06.guitar import Guitar


def main():
    guitars = []

    print("My guitar!")
    guitar_name = input("Name: ")
    while guitar_name != "":
        manufactured_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        add_guitar = Guitar(guitar_name, manufactured_year, guitar_cost)
        guitars.append(add_guitar)
        print(f"{guitar_name} ({manufactured_year}) : ${guitar_cost:.2f} added.")
        guitar_name = input("Name: ")

    for i, guitar in enumerate(guitars, 1):
        guitar.get_age()
        vintage_guitar = guitar.is_vintage()
        if vintage_guitar:
            vintage_guitar = "Vintage"
            print(f"Guitar {i}: {guitar.name} ({guitar.year}), worth $ {guitar.cost} ({vintage_guitar})")
        else:
            print(f"Guitar {i}: {guitar.name} ({guitar.year}), worth $ {guitar.cost}")




main()

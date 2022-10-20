"""
Wimbledon
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    records = get_records(FILENAME)
    champions_to_count, countries = process_records(records)
    display_results(champions_to_count, countries)


def process_records(records):
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_to_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_count[record[INDEX_CHAMPION]] = 1
        return champion_to_count, countries


def display_results(champion_to_count, countries):
    print(f"Wimbledon Champions: ", end=" ")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def get_records(FILENAME):
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Remove header
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()

"""
the champions and how many times they have won.
the countries of the champions in alphabetical order
"""

def get_information():
    stored = []
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            line = line.strip()
            parts = line.split(',')
            stored.append(parts)
    in_file.close()
    print(stored)
    return stored

def process_records(records):
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[1])
        try:
            champion_to_count[record[2]] += 1
        except KeyError:
            champion_to_count[record[2]] = 1
    print(champion_to_count, countries)
    return champion_to_count, countries

process_records(get_information())

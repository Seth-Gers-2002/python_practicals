def process_records(records):
    champion_wins = {}
    countries = set()
    for record in records:
        countries.add(record[1])
        try:
            champion_wins[record[2]] += 1
        except KeyError:
            champion_wins[record[2]] = 1
    return champion_wins, countries


def get_information():
    list_of_wimbledon_winners = []
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            line = line.strip()
            parts = line.split(',')
            list_of_wimbledon_winners.append(parts)
    in_file.close()
    return list_of_wimbledon_winners


def display_info(champion_wins, countries):
    for name, number in champion_wins.items():
        print(name, number)
    print(",".join(country for country in sorted(countries)))


a = get_information()
b = process_records(a)
display_info(b[0], b[1])

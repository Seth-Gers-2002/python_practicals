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
    return stored



get_information()

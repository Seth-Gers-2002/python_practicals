from prac6.guitar import Guitar
import csv


guitars = []
raw_guitars = []

with open("guitars.csv", "r", encoding="utf-8-sig") as in_file:
    in_file.readline()
    for line in in_file:
        line = line.strip()
        parts = line.split(',')
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])
        raw_guitars.append((name, year, cost))
        guitars.append(Guitar(name, year, cost))

    in_file.close()

name = input("name:")
while name != "":
    year = int(input("year:"))
    cost = float(input("cost:"))
    print(name, year, cost)
    details = Guitar(name, year, cost)
    raw_guitars.append((name, year, cost))
    guitars.append(details)
    name = input("name:")

if guitars:
    guitars.sort()
    print("guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(guitar)
    with open('guitars.csv', 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(raw_guitars)
    out_file.close()













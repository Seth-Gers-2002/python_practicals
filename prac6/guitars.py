from prac6.guitar import Guitar

def main():
    guitars = []

    name = input("name:")
    while name != "":
        year = int(input("year:"))
        cost = float(input("cost:"))
        print(f"{name} ({year}) : ${cost}")
        details = Guitar(name, year, cost)
        guitars.append(details)
        name = input("name:")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        guitars.sort()
        print("guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}{2}".format(i, guitar, vintage_string))
    else:
        print("No guitars")
main()
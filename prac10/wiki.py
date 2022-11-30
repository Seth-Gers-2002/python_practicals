import wikipedia


def main():
    print("would you like to search(s), summary(m) or the page(p) of something")
    choice = input(">>>").upper()
    print("Please enter a name, location, item or term")
    search = input(">>>")
    while choice != "":
        if choice == "S":
            print(wikipedia.search(search))
        elif choice == "M":
            print(wikipedia.summary(search))
        elif choice == "P":
            print(wikipedia.page(search))
        else:
            print("please input an appropriate search term")

        print("would you like to search(s), summary(m) or the page(p) of something")
        choice = input(">>>").upper()
        print("Please enter a name, location, item or term")
        search = input(">>>")


main()

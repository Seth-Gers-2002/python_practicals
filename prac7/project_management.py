"""
Seth Gersbach
"""

import csv
import datetime
projects = []


def Option_display():
    options = ("L:load projects", "S:save projects", "D:display projects", "F:filiter projects by date", "A:add new project", "U:update project")
    for i in options:
        print(i)


def Add_Info():
    """Add data to the set"""
    while True:
        try:
            name = input("Project name: ")
            date = input("Project start date (dd/mm/yyyy):")
            priority = input("priority: (int)")
            cost = input("cost (float):")
            percentage = input("completion percentage (int):")
            info = ([name, date, priority, cost, percentage])
            return info
        except ValueError or IndexError:
            print("Incorrect, input again")

Option_display()

choice = input(">>>").upper()


while choice != "S":
    if choice == "L":
        with open("projects.csv", "r", encoding="utf-8-sig") as in_file:
            """Gets information from csv then saves the raw and processed information"""
            in_file.readline()
            for line in in_file:
                line = line.strip()
                parts = line.split('\t')
                projects.append(parts)
            in_file.close()
    if choice == "D":
        """Displays menu input options"""
        if projects:
            stored = []
            print("Incomplete projects: ")
            for project in projects:
                if project[4] != '100':
                    print(", ".join(project))
                elif project[4] == '100':
                    stored.append(project)
            if stored:
                print("Completed projects")
                for store in stored:
                    print(", ".join(store))
        else:
            print("nothing to print")
    if choice == "A":
        projects.append(Add_Info())
    if choice == "U":
        i = 1
        for project in projects:
            print(f"{i} ", ", ".join(project))
            i += 1
        """Update and reorganise the data"""
        if projects:
            project_number = int(input("input project number:")) - 1
            print(", ".join(projects[project_number]))
            change = input("P:change priority or C:change percentage or O:To leave").upper()
            if change == "P":
                projects[[project_number][2]] = int(input("priority:"))
            elif change == "C":
                projects[[project_number][4]] = int(input("percentage"))
        else:
            print("nothing to print")
    if choice == "F":
        date_string = input("Date (dd/mm/yyyy): ")
        search_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        for dates in projects:
            check_date = datetime.datetime.strptime(dates[1], "%d/%m/%Y").date()
            if check_date == search_date:
                print(dates)

    Option_display()
    choice = input(">>>").upper()

with open('projects.csv', 'w', newline='') as out_file:
    writer = csv.writer(out_file)
    writer.writerows(projects)
out_file.close()


import csv

options = ("L:load projects", "S:save projects", "D:display projects", "F:filiter projects by date", "A:add new project", "U:update project")
projects = []

while choice != "Q":

    for i in options:
        print(i)

    choice = input(">>>").upper()
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
        if projects:
            i = 1
            for project in projects:
                print(f"{i} ", ", ".join(project))
                i += 1
        else:
            print("nothing to print")
    choice = input(">>>").upper()
    if choice == "A":
        name = input("Project name: ")
        date = input("Project start date:")
        priority = input("priority:")
        cost = float(input("cost:"))
        percentage = input("completion percentage:")
        projects.append([name, date, priority, cost, percentage])
    if choice == "U":
        try:
            project_number = int(input("input project number:")) - 1
            change = input("P:change priority or C:change percentage or O:To leave").upper()
        except ValueError:
            print("incorrect value")
        if change == "P":
            projects[project_number][2] = int(input("priority:"))
        elif change == "C":
            projects[project_number][4] = int(input("percentage"))



    """
    save projects
    filter projects by date
    """





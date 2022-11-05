import csv

print("load projects, save projects, display projects, filiter projects by date, add new project, update project")
projects = []
choice = input(">>>").upper()

while choice != "Q":
    if choice == "L":
        with open("guitars.csv", "r", encoding="utf-8-sig") as in_file:
            """Gets information from csv then saves the raw and processed information"""
            in_file.readline()
            for line in in_file:
                line = line.strip()
                parts = line.split(',')
                projects.append(parts)
            in_file.close()
    if choice == "D":
        print(projects)
    choice = input(">>>").upper()

    """
    save projects
    filter projects by date
    add new project 
    update project
    """





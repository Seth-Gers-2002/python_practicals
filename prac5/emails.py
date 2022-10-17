
def main():
    email_to_name = get_name_and_email()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def check_if_name_is_correct(name):
    name_check = input("(Y/n):")
    if name_check == "Y" or name_check == "y" or name_check == "yes" or name_check == "Yes":
        return name
    elif name_check == "N" or name_check == "n" or name_check == "no" or name_check == "No":
        name_correct = input("So what is your name? ").title()
        return name_correct


def get_name_and_email():
    email_to_name = {}
    email = input("Email: ")
    email_split = email.split("@")

    while email != "":
        if "." in email_split[0]:
            name = email_split[0].replace(".", " ").title()
        else:
            name = email_split[0].title()

        print(f"is your name {name}?")
        name_checked = check_if_name_is_correct(name)
        email_to_name[email] = name_checked

        email = input("Email: ")
        email_split = email.split("@")
    return email_to_name


main()

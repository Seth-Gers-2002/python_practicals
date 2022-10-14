
email = input("Email: ")

email_split = email.split("@")
if "." in email_split[0]:
    name = email_split[0].split(".")
    print(f"is your name {name[0]},{name[1]}")
else:
    print(email_split)
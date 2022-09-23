
password = input("password:")
while len(password) <= 10:
    print("invaild")
    password = input("password:")

print("*" * len(password))
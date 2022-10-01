"""
program gets a password and censors it over a certain length
"""


def get_password(password):
    """Check the length of the password"""
    while len(password) <= 9:
        password = input("Invalid password: ")
    return password


password = input("password:")
print("*" * len(get_password(password)))

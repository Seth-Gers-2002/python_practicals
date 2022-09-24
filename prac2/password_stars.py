def main():
    password = get_password()

    print_censor(password)


def print_censor(password):
    print("*" * len(password))


def get_password():
    password = input("password:")
    while len(password) <= 9:
        print("invaild")
        password = input("password:")
    return password


main()

"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting


"""


def main():
    code_to_name = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
                    "WA": "Western Australia",
                    "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
    max_length = max(len(name) for name in code_to_name)

    state_code = input("Enter short state: ").upper()
    while state_code != "":
        try:
            print(f"{state_code:{max_length}} is {code_to_name[state_code]}")
        except:
            print("incorrect phrase")
        state_code = input("Enter short state: ").upper()
        # if state_code in code_to_name:
        #     print(f"{state_code:{max_length}} is {code_to_name[state_code]}")
        # else:
        #     print("Invalid short state")
        # state_code = input("Enter short state: ").upper()


main()

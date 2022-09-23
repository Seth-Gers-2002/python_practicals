"""
display options,
loop
user select
quit
"""

print("H:Hello, G:Goodbye, Q:Quit:, O:Options")
choice = str(input("Enter value (O for Options): "))
while choice != "Q":
    if choice == "H":
        print("hello")
    elif choice == "G":
        print("goodbye")
    elif choice == "O":
        print("TYPE H for Hello, G for Goodbye, Q for Quit:, O for Options")
    else:
        print("Invalid choice... H:Hello, G:Goodbye, Q:Quit:, O:Options")

    choice = (input("Enter value (O for Options): "))

print("farewell")
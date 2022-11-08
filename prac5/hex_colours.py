hex_colours = {"absolutezero": "#0048ba", "acidgreen": "#b0bf1a", "aliceblue": "#f0f8ff", "alizarincrimson": "#e32636",
               "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc", "antiquewhite": "#faebd7"}

get_colour = input("what colour?").lower().replace(" ", "")

while get_colour != "":
    if correct_get_colour in hex_colours:
        print(f"{get_colour} is {hex_colours[correct_get_colour]}")
    else:
        print("Invalid colour-name")
    get_colour = input("what colour?")
    correct_get_colour = get_colour.lower().replace(" ", "")
key = lambda x: x[1]

hex_colours = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue":"#f0f8ff", "Alizarin crimson": "#e32636", "Amaranth":"#e52b50"}

get_colour = input("what colour?")

while get_colour != " ":
    if get_colour in hex_colours:
        print(f"{get_colour:{10}} is {hex_colours[get_colour]}")
    else:
        print("Invalid colourname")
    get_colour = input("what colour?")

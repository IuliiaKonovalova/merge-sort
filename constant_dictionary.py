
def coloured_square(hex_string):
    """
    Returns a coloured square that you can print to a terminal.
    Based on: https://alexwlchan.net/2021/coloured-squares/
    """
    hex_string = hex_string.strip("#")
    assert len(hex_string) == 6
    red = int(hex_string[:2], 16)
    green = int(hex_string[2:4], 16)
    blue = int(hex_string[4:6], 16)
    colored_square = f"\033[48;2;{red};{green};{blue}m \033[49m"  # Colored square
    output = ""
    for _ in range(2):
        row = colored_square  # Repeat the colored square horizontally
        output += f"{row}"  # Add the row to the output

    return output


constants = {
    0: coloured_square("#FFFFFF"),
    1: coloured_square("#ffbaba"),
    2: coloured_square("#ff7b7b"),
    3: coloured_square("#ff5252"),
    4: coloured_square("#FF0000"),
    5: coloured_square("#a70000"),
    6: coloured_square("#B32100"),
    7: coloured_square("#BF4200"),
    8: coloured_square("#DF7000"),
    9: coloured_square("#FF9D00"),
    10: coloured_square("#FFFF00"),
    11: coloured_square("#FCE762"),
    12: coloured_square("#80C000"),
    13: coloured_square("#408E00"),
    14: coloured_square("#005B00"),
    15: coloured_square("#004540"),
    16: coloured_square("#002E80"),
    17: coloured_square("#0017C0"),
    18: coloured_square("#0000FF"),
    19: coloured_square("#869EFF"),
    20: coloured_square("#D7DFFF"),
    21: coloured_square("#D2C0E0"),
    22: coloured_square("#A580C1"),
    23: coloured_square("#7840A2"),
    24: coloured_square("##8A20D1"),
    25: coloured_square("#9C00FF"),
    26: coloured_square("#4B0082"),
    27: coloured_square("#390062"),
    28: coloured_square("#260041"),
    29: coloured_square("#1D0031"),
    30: coloured_square("#130021"),
    31: coloured_square("#000000"),
}


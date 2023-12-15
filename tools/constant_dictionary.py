
def colored_square(hex_string):
    """
    Returns a coloured square that you can print to a terminal.
    Based on: https://alexwlchan.net/2021/coloured-squares/
    """
    hex_string = hex_string.strip("#")
    assert len(hex_string) == 6
    red = int(hex_string[:2], 16)
    green = int(hex_string[2:4], 16)
    blue = int(hex_string[4:6], 16)
    # Colored square with the given RGB values
    colored_square = f"\033[48;2;{red};{green};{blue}m \033[49m"
    output = ""
    for _ in range(2):
        row = colored_square  # Repeat the colored square horizontally
        output += f"{row}"  # Add the row to the output

    return output


constants_3 = {
    0: colored_square("#FFFFFF"), # White
    1: colored_square("#ffbaba"),
    2: colored_square("#ff7b7b"),
    3: colored_square("#ff5252"),
    4: colored_square("#FF0000"),
    5: colored_square("#a70000"), # Dark Red
    6: colored_square("#B32100"),
    7: colored_square("#BF4200"),
    8: colored_square("#DF7000"),
    9: colored_square("#FF9D00"),
    10: colored_square("#FFFF00"), # Yellow
    11: colored_square("#FCE762"),
    12: colored_square("#80C000"),
    13: colored_square("#408E00"),
    14: colored_square("#005B00"),
    15: colored_square("#004540"),
    16: colored_square("#002E80"), # Blue
    17: colored_square("#0017C0"),
    18: colored_square("#0000FF"),
    19: colored_square("#869EFF"),
    20: colored_square("#D7DFFF"), # Light Blue
    21: colored_square("#D2C0E0"),
    22: colored_square("#A580C1"),
    23: colored_square("#7840A2"),
    24: colored_square("#8A20D1"), # Purple
    25: colored_square("#9C00FF"),
    26: colored_square("#4B0082"),
    27: colored_square("#390062"),
    28: colored_square("#260041"), # Dark Purple
    29: colored_square("#1D0031"),
    30: colored_square("#130021"),
    31: colored_square("#000000"), # Black
}


constants_2 = {
    0: colored_square("#000D33"),  # Dark Blue
    1: colored_square("#002555"),
    2: colored_square("#00477A"),
    3: colored_square("#00669F"),
    4: colored_square("#0085C4"),
    5: colored_square("#009BDC"),
    6: colored_square("#00B2F3"),
    7: colored_square("#00C6FF"),
    8: colored_square("#4DC7FF"),
    9: colored_square("#99DAFF"),
    10: colored_square("#C9EBFF"),
    11: colored_square("#FFFFFF"),  # White
    12: colored_square("#CCCCCC"),
    13: colored_square("#999999"),
    14: colored_square("#666666"),
    15: colored_square("#333333"),
    16: colored_square("#000000"),  # Black
}


constants_1 = {
    0: colored_square("#FFFF00"),  # Yellow
    1: colored_square("#FFCC00"),
    2: colored_square("#FF9900"),
    3: colored_square("#FF6600"),
    4: colored_square("#FF3300"),
    5: colored_square("#FF0000"),  # Red
    6: colored_square("#E60000"),
    7: colored_square("#CC0000"),
    8: colored_square("#B30000"),
    9: colored_square("#8B0000"),  # Dark Red
}
[{}, {}, {}]
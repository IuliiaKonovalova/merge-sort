
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


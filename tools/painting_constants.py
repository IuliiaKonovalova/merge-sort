"""This file contains constants for colorama."""
# from colorama import Fore, Back, Style
from blessed import Terminal
term = Terminal()

# white = Fore.WHITE
# green = Fore.GREEN
# blue = Fore.BLUE
# yellow = Fore.YELLOW
# magenta = Fore.MAGENTA
# cyan = Fore.CYAN
# red = Fore.RED
# black = Fore.BLACK


# b_gr_f_ye = Back.GREEN + Fore.YELLOW 
# b_bl_f_ye = Back.BLUE + Fore.YELLOW

# b_black = Back.BLACK
# b_red = Back.RED
# b_green = Back.GREEN
# b_yellow = Back.YELLOW
# b_blue = Back.BLUE
# b_magenta = Back.MAGENTA
# b_cyan = Back.CYAN
# b_white = Back.WHITE

# dim = Style.DIM

# reset = Style.RESET_ALL


white = term.white
green = term.green3
blue = term.deepskyblue2
yellow = term.yellow
magenta = term.magenta
cyan = term.cyan
red = term.red
black = term.black
lightgreen = term.lightgreen
darkviolet = term.darkviolet
purple3 = term.purple3

b_black = term.on_black
b_red = term.on_red
b_green = term.on_green
b_yellow = term.on_yellow
b_blue = term.on_deepskyblue2
b_blue2 = term.on_blue
b_magenta = term.on_magenta
b_cyan = term.on_cyan
b_white = term.on_white
b_plum2 = term.on_plum2
b_steelblue2 = term.on_steelblue2
b_lightgreen = term.on_lightgreen
b_forestgreen = term.on_forestgreen
b_steelblue3 = term.on_steelblue3
b_dodgerblue2 = term.on_dodgerblue2
b_purple1 = term.on_purple1

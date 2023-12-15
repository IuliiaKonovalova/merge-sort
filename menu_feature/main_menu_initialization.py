from simple_term_menu import TerminalMenu
from menu_feature.menu_constants import *


main_menu = TerminalMenu(options)


def show_main_menu():
    options_index = main_menu.show()
    options_choice = options[options_index]
    return options_choice

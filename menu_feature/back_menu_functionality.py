from core_imports.core_imports import *
from menu_feature.menu_constants import *
from menu_feature.menu_functionality import menu_logic


def show_back_menu():
    """
    Displays the back menu
    Args:
        None
    Returns:
        None
    """
    back_menu = TerminalMenu(back_options)
    back_menu_index = back_menu.show()
    back_menu_choice = back_options[back_menu_index]
    if back_menu_choice == '1. Back':
        system('clear')
        menu_logic()
    elif back_menu_choice == '2. Exit':
        exit()

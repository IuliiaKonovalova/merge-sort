from simple_term_menu import TerminalMenu
from menu_feature.menu_constants import back_options


def show_back_menu():
    back_menu = TerminalMenu(back_options)
    back_menu_index = back_menu.show()
    back_menu_choice = back_options[back_menu_index]
    if back_menu_choice == '1. Back':
        from menu_feature.menu_functionality import menu_logic
        menu_logic()
    elif back_menu_choice == '2. Exit':
        exit()

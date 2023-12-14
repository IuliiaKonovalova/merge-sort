from simple_term_menu import TerminalMenu
from menu_feature.menu_constants import *
from menu_feature.list_length_options_initialization import *
from menu_feature.display_code_control import *


algorithm_options_menu = TerminalMenu(algorithm_options)


def show_algorithm_options_menu(algorithm_options_name):
    print(f"""{algorithm_options_name.upper()}""")
    algorithm_options_index = algorithm_options_menu.show()
    algorithm_options_choice = algorithm_options[algorithm_options_index]
    if algorithm_options_choice == '1. Animation':
        show_list_length_options_menu(algorithm_options_name, 'animation')
    elif algorithm_options_choice == '2. Step by step':
        show_list_length_options_menu(algorithm_options_name, 'step by step')
    elif algorithm_options_choice == '3. Code':
        show_algorithm_code(algorithm_options_name)

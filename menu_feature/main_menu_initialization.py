from simple_term_menu import TerminalMenu
from menu_feature.menu_constants import *


main_menu = TerminalMenu(options)
# algorithm_options_menu = TerminalMenu(algorithm_options)
# list_length_options_menu = TerminalMenu(list_length_options)

def show_main_menu():
    options_index = main_menu.show()
    options_choice = options[options_index]
    return options_choice



# def show_algorithm_menu(algorithm_name):
#     print(f"""{algorithm_name.upper()}""")
#     algorithm_options_index = algorithm_options_menu.show()
#     algorithm_choice = algorithm_options[algorithm_options_index]
#     return algorithm_choice


# def show_list_length_options_menu():
#     list_length_options_index = list_length_options_menu.show()
#     list_length_options_choice = list_length_options[list_length_options_index]
#     return list_length_options_choice
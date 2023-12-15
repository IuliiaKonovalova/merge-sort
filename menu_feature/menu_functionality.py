
from menu_feature.main_menu_initialization import *
from menu_feature.algorithms_options_menu_initialization import *
from tools.constant_dictionary import *


def menu_logic():
    """
    Runs the merge sort algorithm implementation
    Asks user for a list of comma separated numbers
    """
    quitting = False
    while quitting is not True:
        options_choice = show_main_menu()
        if options_choice == 'Quit':
            print(f'''QUITTING...''')
            quitting = True
        else:
            show_algorithm_options_menu(options_choice)

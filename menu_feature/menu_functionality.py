
from menu_feature.main_menu_initialization import *
from menu_feature.algorithms_options_menu_initialization import *

# from menu_feature.menu_constants import *
from tools.constant_dictionary import *
# from test_cases import *
# from display_code.merge_sort_code.merge_sort import *
# from display_code.selection_sort_code.selection_sort import *
# from display_code.insertion_sort_code.insertion_sort import *
# from display_code.bubble_sort_code.bubble_sort import *
# from display_code.quick_sort_code.quick_sort import *
from test_cases import show_bubble_sort_animation_with_constants, show_bubble_sort_with_constants, show_insertion_sort_animation_with_constants, show_insertion_sort_with_constants, show_merge_sort_animation_with_constants, show_merge_sort_with_constants, show_quick_sort_animation_with_constants, show_quick_sort_with_constants, show_selection_sort_animation_with_constants, show_selection_sort_with_constants


def menu_logic():
    """
    Runs the merge sort algorithm implementation
    Asks user for a list of comma separated numbers
    """
    quitting = False
    while quitting is not True:
        options_choice = show_main_menu()
        if options_choice == '6. Quit':
            print(f'''QUITTING...''')
            quitting = True
        elif options_choice == '1. Merge Sort':
            show_algorithm_options_menu('merge sort')
        elif options_choice == '2. Selection Sort':
            show_algorithm_options_menu('selection sort')
        elif options_choice == '3. Insertion Sort':
            show_algorithm_options_menu('insertion sort')
        elif options_choice == '4. Bubble Sort':
            show_algorithm_options_menu('bubble sort')
        elif options_choice == '5. Quick Sort':
            show_algorithm_options_menu('quick sort')

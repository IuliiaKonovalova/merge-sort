from display_code.selection_sort_code.selection_sort import *
from display_code.merge_sort_code.merge_sort import *
from display_code.insertion_sort_code.insertion_sort import *
from display_code.quick_sort_code.quick_sort import *
from display_code.bubble_sort_code.bubble_sort import *


def show_algorithm_code(algorithm_options_name):
    """
    Displays the code of the algorithm
    Args:
        algorithm_options_name (str): name of the algorithm
    Returns:
        None
    """
    if algorithm_options_name == 'Merge Sort':
        display_merge_sort_code()
    elif algorithm_options_name == 'Selection Sort':
        display_selection_sort_code()
    elif algorithm_options_name == 'Insertion Sort':
        display_insertion_sort_code()
    elif algorithm_options_name == 'Quick Sort':
        display_quick_sort_code()
    elif algorithm_options_name == 'Bubble Sort':
        display_bubble_sort_code()
    sleep(2)
    show_back_menu()

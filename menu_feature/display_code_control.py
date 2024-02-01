from core_imports.display_code_imports import *
from menu_feature.back_menu_functionality import show_back_menu


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

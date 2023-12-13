import random
from tools.print_items import print_items


def generate_unsorted_list_from_constants(constants, sort_algorithm_name):
    """
    Generates an unsorted list of numbers
    Args:
        constants (dict): dictionary of constants
        sort_algorithm_name (str): name of the sort algorithm
    Returns:
        unsorted_list (list): unsorted list of numbers
    """
    unsorted_list = []
    for key in constants:
        unsorted_list.append(key)
    random.shuffle(unsorted_list)
    print(sort_algorithm_name)
    print(unsorted_list)
    print_items(unsorted_list, constants)
    return unsorted_list

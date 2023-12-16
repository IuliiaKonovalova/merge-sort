import os
from time import sleep
from tools.print_items import print_items


def split_list(initial_list, constants):
    """
    Splits a list into 2 parts
    Args:
        initial_list (list): list of numbers
    Returns:
        left_part (list): left part of the list
        right_part (list): right part of the list
    """
    os.system('clear')
    print("MERGE SORT ANIMATION\n")
    print("TO BE SPLIT: ", initial_list)
    print_items(initial_list, constants)
    sleep(1.5)

    mid_point = len(initial_list) // 2
    left_part = initial_list[:mid_point]
    print("\n LEFT: ", left_part)

    print_items(left_part, constants)
    print("\n")
    right_part = initial_list[mid_point:]
    print("\n RIGHT: ", right_part)
    print_items(right_part, constants)
    print("\n")
    sleep(1.5)
    os.system('clear')
    print("MERGE SORT ANIMATION\n")

    return left_part, right_part

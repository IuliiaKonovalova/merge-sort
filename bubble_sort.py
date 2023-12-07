import time
import os
from print_items import print_items

unorder_list  = [3, 1, 4]

def bubble_sort(unord_list):
    """
    Sorts a list of numbers using bubble sort algorithm
    Args:
        initial_list (list): list of numbers
    Returns:
        initial_list (list): sorted list of numbers
    """
    for i in range(len(unord_list) - 1):
        for j in range(len(unord_list) - 1):
            if unord_list[j] > unord_list[j + 1]:
                unord_list[j], unord_list[j + 1] = unord_list[j + 1], unord_list[j]

    return unord_list
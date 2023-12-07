import time
import os
from print_items import print_items

unord_list  = [3, 1 4]

def bubble_sort(initial_list, constants):
    """
    Sorts a list of numbers using bubble sort algorithm
    Args:
        initial_list (list): list of numbers
    Returns:
        initial_list (list): sorted list of numbers
    """
    for i in range(len(initial_list) - 1):
        for j in range(len(initial_list) - 1):
            if initial_list[j] > initial_list[j + 1]:
                initial_list[j], initial_list[j + 1] = initial_list[j + 1], initial_list[j]
                print_items(initial_list, constants)
                time.sleep(0.9)
                os.system('clear')
    return initial_list
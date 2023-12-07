import os
import time
from print_items import print_items, print_temp_item
from constant_dictionary import *


def insertion_sort_animation(list_data, constants):
    """
    Sorts a list of numbers using insertion sort algorithm
    Args:
        initial_list (list): list of numbers
    Returns:
        initial_list (list): sorted list of numbers
    """
    for scan_index in range(1, len(list_data)):
        temp = list_data[scan_index]
        min_index = scan_index
        while min_index > 0 and temp < list_data[min_index - 1]:
            list_data[min_index] = list_data[min_index - 1]
            min_index -= 1
            list_data[min_index] = temp
            printing_animation(temp, list_data, constants)
        printing_animation(temp, list_data, constants)
    return list_data


def printing_animation(temp, list_data, constants):
    """
    Prints the animation of insertion sort
    Args:
        initial_list (list): list of numbers
    Returns:
        initial_list (list): sorted list of numbers
    """
    os.system('clear')
    print("INSERTION SORT ANIMATION")
    print("\n TEMP: ", temp)
    print_temp_item(temp, list_data, constants)
    print("\n Sorting...")
    print_items(list_data, constants)
    time.sleep(0.9)

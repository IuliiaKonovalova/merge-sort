import os
from time import sleep
from tools.print_items import print_items, print_temp_item
from tools.constant_dictionary import *
from tools.colorama_constants import *


def selection_sort_animation(list_data, constants):
    """
    Sorts a list of numbers using selection sort algorithm
    Args:
        initial_list (list): list of numbers
    Returns:
        initial_list (list): sorted list of numbers
    """
    for scan_index in range(0, len(list_data)):
        min_index = scan_index
        print("SELECTION SORT ANIMATION")
        # printing_animation(min_index, list_data, constants)
        # for printing the animation
        comp_index = 0
        printing_animation(min_index, scan_index, comp_index, list_data, constants)
        for comp_index in range(scan_index + 1, len(list_data)):
            printing_animation(min_index, scan_index, comp_index, list_data, constants)
            if list_data[comp_index] < list_data[min_index]:
                printing_animation(min_index, scan_index, comp_index, list_data, constants)
                min_index = comp_index
                printing_animation(min_index, scan_index, comp_index, list_data, constants)
        if min_index != scan_index:
            list_data[scan_index], list_data[min_index] = (
                list_data[min_index], list_data[scan_index]
            )
            printing_animation(min_index, scan_index, comp_index, list_data, constants)
    return list_data


def printing_animation(min_index, scan_index, comp_index, list_data, constants):
    """
    Prints the animation of selection sort
    Args:
        initial_list (list): list of numbers
    Returns:
        initial_list (list): sorted list of numbers
    """
    os.system('clear')
    print("SELECTION SORT ANIMATION")
    print("\n MIN_INDEX")
    print_temp_item(min_index, list_data, constants)
    print("\n")
    print("LIST DATA AFTER SORT: ", end="")
    print_list_with_pointers(list_data, scan_index, comp_index, min_index)
    print_items(list_data, constants)
    sleep(0.2)


def print_list_with_pointers(list_data, scan_index, comp_index, min_index):

    last_index = len(list_data) - 1
    print("[", end="")
    for k, item in enumerate(list_data):
        if k != last_index:
            if k == scan_index and min_index == scan_index:
                print(term.on_bright_yellow(term.green(str(item))), end=", ")
            elif k == scan_index and min_index != scan_index:
                print(b_forestgreen(str(item)), end=", ")
            elif k == min_index and min_index == comp_index:
                print(term.on_bright_yellow(term.darkviolet(str(item))), end=", ")
            elif k == min_index:
                print(b_yellow(str(item)), end=", ")
            elif k == comp_index:
                print(b_purple1(str(item)), end=", ")
            else:
                print(white(str(item)), end=", ")
        elif k == last_index:
            if k == scan_index and min_index == scan_index:
                print(term.on_bright_yellow(term.green(str(item))), end="")
            elif k == scan_index and min_index != scan_index:
                print(b_forestgreen(str(item)), end="")
            elif k == min_index and min_index == comp_index:
                print(term.on_bright_yellow(term.darkviolet(str(item))), end="")
            elif k == min_index:
                print(b_yellow(str(item)), end="")
            elif k == comp_index:
                print(b_purple1(str(item)), end="")
            else:
                print(white(str(item)), end="")
    print("]")

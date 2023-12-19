import os
from time import sleep
from tools.print_items import *
from tools.constant_dictionary import *


def quick_sort_animation(list_data, constants):
    """
    Sorts a list of numbers using quick sort algorithm
    Args:
        list_data (list): list of numbers
    Returns:
        list_data (list): sorted list of numbers
    """
    quick_sort_recursive(list_data, 0, len(list_data) - 1, constants)
    return list_data


def quick_sort_recursive(list_data, low, high, constants):
    """
    Recursive function for quick sort
    """
    if low < high:
        pivot_index = partition(list_data, low, high, constants)
        quick_sort_recursive(list_data, low, pivot_index - 1, constants)
        quick_sort_recursive(list_data, pivot_index + 1, high, constants)


def partition(list_data, low, high, constants):
    """
    Partitioning step in quick sort
    """
    pivot = list_data[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if list_data[j] <= pivot:
            list_data[i], list_data[j] = list_data[j], list_data[i]
            i += 1
            animation_control(list_data, pivot, i - 1, j, low, high, constants)
    list_data[low], list_data[i - 1] = list_data[i - 1], list_data[low]
    animation_control(list_data, pivot, i - 1, high, low, high, constants)
    return i - 1


def animation_control(list_data, pivot, pivot_index, current_index, low, high, constants):
    """ Prints the animation of quick sort """
    os.system('clear')
    print("QUICK SORT ANIMATION")
    print("\n Pivot: ", pivot)
    print("\n Current Index: ", current_index)
    print_temp_item(current_index, list_data, constants)
    print("\n Low: ", low)
    print("\n High: ", high)
    print_items(list_data, constants)
    sleep(0.9)

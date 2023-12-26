import os
from time import sleep
from tools.print_items import *
from tools.constant_dictionary import *
from tools.painting_constants import *


def quick_sort_animation(list_data, constants, temp_list):
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
    print_list_with_pointers(list_data, pivot_index, low, high)
    print("\n Low: ", low)
    print("\n High: ", high)
    print_items(list_data, constants)
    sleep(2.9)


def print_list_with_pointers(list_data, pivot, low, high):
    """
    Prints the items in a list
    Args:
        list_data (list): list of numbers
        pivot (int): pivot
        low (int): low
        high (int): high
    Returns:
        None
    """
    print("[", end="")
    for i in range(len(list_data)):
        if i == pivot:
            print(f"{yellow}{list_data[i]}{white}", end="")
        elif i == low:
            print(f"{green}{list_data[i]}{white}", end="")
        elif i == high:
            print(f"{blue}{list_data[i]}{white}", end="")
        else:
            print(list_data[i], end="")
        if i != len(list_data) - 1:
            print(", ", end="")
    print("]")


def print_list_to_merge(less_than_pivot, pivot, greater_than_pivot):
    """
    Prints the less than pivot and greater than pivot
    Args:
        less_than_pivot (list): list of numbers less than the pivot
        pivot (int): the pivot
        greater_than_pivot (list): list of numbers greater than the pivot
    Returns:
        None
    """
    print(
        f"""{green}{less_than_pivot}{white}""", end=" + "
    )
    print(
        f"""{yellow}{pivot}{white}""", end=" + "
    )
    print(
        f"""{blue}{greater_than_pivot}{white}"""
    )
    print()
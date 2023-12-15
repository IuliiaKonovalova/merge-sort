import os
from time import sleep
from tools.print_items import print_items
from tools.constant_dictionary import *


def quick_sort_animation(arr, constants):
    """
    Sorts a list of numbers using quick sort algorithm
    Args:
        arr (list): list of numbers
    Returns:
        arr (list): sorted list of numbers
    """
    quick_sort_recursive(arr, 0, len(arr) - 1, constants)
    return arr


def quick_sort_recursive(arr, low, high, constants):
    """
    Recursive function for quick sort
    """
    if low < high:
        pivot_index = partition(arr, low, high, constants)
        quick_sort_recursive(arr, low, pivot_index - 1, constants)
        quick_sort_recursive(arr, pivot_index + 1, high, constants)


def partition(arr, low, high, constants):
    """
    Partitioning step in quick sort
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            printing_animation(arr, pivot, i, j, low, high, constants)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    printing_animation(arr, pivot, i + 1, high, low, high, constants)
    return i + 1


def printing_animation(arr, pivot, pivot_index, current_index, low, high, constants):
    """ Prints the animation of quick sort """
    os.system('clear')
    print("QUICK SORT ANIMATION")
    print("\n Pivot: ", pivot)
    print("\n Current Index: ", current_index)
    print("\n Low: ", low)
    print("\n High: ", high)
    print_items(arr, constants)
    sleep(0.9)

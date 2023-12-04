import os
import time
from print_items import print_items


def merge(left, right, constants):
    """
    Takes 2 lists and analyzes them to sort them in ascending order
    Args:
        left (list): list of numbers
        right (list): list of numbers
    Returns:
        sorted_list (list): list of numbers sorted in ascending order
    """
    sorted_list = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    # append the remaining elements from left that was not fully iterated
    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    # append the remaining elements from right that was not fully iterated
    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    print("\nSORTED and MERGED LIST: ", sorted_list)
    print_items(sorted_list, constants)
    print("\n")

    # check if the sorted_list is sorted
    if sorted(sorted_list) == sorted_list:
        print("\n")
        print("SORTED LIST: ", sorted_list)
        print_items(sorted_list, constants)
    return sorted_list

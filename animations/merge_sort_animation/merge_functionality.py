import os
from time import sleep
from tools.colorama_constants import *
from tools.print_items import print_items

def merge(left, right, constants, temp_list):
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
    sleep(1.5)
    os.system('clear')
    print(
      f"""{yellow}MERGE SORT ANIMATION{white}
      """
    )
    if len(temp_list) == len(sorted_list):
        print("FINAL SORTED LIST: ", sorted_list)
        print_items(sorted_list, constants)

    return sorted_list

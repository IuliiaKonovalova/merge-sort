import os
from time import sleep
from tools.colorama_constants import *
from tools.print_items import print_items
from animations.merge_sort_animation.split_functionality import split_list
from animations.merge_sort_animation.merge_functionality import merge


def merge_sort_animation(initial_list, constants, temp_list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    Takes O(kn log n) time
    """
    if temp_list == initial_list:
        os.system('clear')
        print(
      f"""{yellow}MERGE SORT ANIMATION{white}
      """
        )
        print("INITIAL LIST: ", temp_list)
        print_items(initial_list, constants)
        sleep(1.5)
    if len(initial_list) <= 1:
        return initial_list

    left_half, right_half = split_list(initial_list, constants)
    left = merge_sort_animation(left_half, constants, temp_list)
    print("LEFT: ", left)
    right = merge_sort_animation(right_half, constants, temp_list)
    print("RIGHT: ", right)

    return merge(left, right, constants, temp_list)

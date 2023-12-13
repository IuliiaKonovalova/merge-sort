import random
from merge_sort import merge_sort
from selection_sort import selection_sort
from animations.selection_sort_animation.selection_sort import *
from tools.print_items import print_items
from animations.merge_sort_animation.merge_sort import *
from insertion_sort import insertion_sort
from animations.insertion_sort_animation.insertion_sort import *
from bubble_sort import bubble_sort
from animations.bubble_sort_animation.bubble_sort import *
from quick_sort import quick_sort
from tools.constant_dictionary import *
from animations.quick_sort_animation.quick_sort import *


def generate_unsorted_list_from_constants(constants, sort_algorithm_name):
    """
    Generates an unsorted list of numbers
    :return: an unsorted list of numbers
    """
    unsorted_list = []
    for key in constants:
        unsorted_list.append(key)
    random.shuffle(unsorted_list)
    print(sort_algorithm_name)
    print(unsorted_list)
    print_items(unsorted_list, constants)
    return unsorted_list


def show_merge_sort_with_constants(constants):
    """
    Tests the merge sort algorithm with the constants dictionary
    """
    sort_algorithm_name = "MERGE SORT"
    unsorted_list = generate_unsorted_list_from_constants(constants, sort_algorithm_name)
    temp_list = unsorted_list.copy()
    print(
    f"""
    To compare: 
    Sorted list: {merge_sort(unsorted_list, constants)}
    Initial list: {temp_list}
    """
    )


def show_merge_sort_animation_with_constants(constants):
    """
    Tests the merge sort algorithm with the constants dictionary
    """
    sort_algorithm_name = "MERGE SORT"
    unsorted_list = generate_unsorted_list_from_constants(constants, sort_algorithm_name)
    temp_list = unsorted_list.copy()
    print(
    f"""
    To compare: 
    Sorted list: {merge_sort_animation(unsorted_list, constants)}
    Initial list: {temp_list}
    """
    )


def show_selection_sort_with_constants(constants):
    """
    Tests the merge sort algorithm with the constants dictionary
    """
    sort_algorithm_name = "SELECTION SORT"
    unsorted_list = generate_unsorted_list_from_constants(constants, sort_algorithm_name)
    temp_list = unsorted_list.copy()
    print(
        f"""
    To compare: 
    Sorted list: {selection_sort(unsorted_list, constants)}
    Initial list: {temp_list}
    """
    )


def show_selection_sort_animation_with_constants(constants):
    """
    Tests the merge sort algorithm with the constants dictionary
    """
    sort_algorithm_name = "SELECTION SORT"
    unsorted_list = generate_unsorted_list_from_constants(constants, sort_algorithm_name)
    temp_list = unsorted_list.copy()
    print(
        f"""
    To compare:
    Sorted list: {selection_sort_animation(unsorted_list, constants)}
    Initial list: {temp_list}
    """
    )


def show_insertion_sort_with_constants(constants):
    """
    Tests the merge sort algorithm with the constants dictionary
    """
    sort_algorithm_name = "INSERTION SORT"
    temp_list = unsorted_list.copy()
    unsorted_list = generate_unsorted_list_from_constants(constants, sort_algorithm_name)
    print(
        f"""
    To compare:
    Sorted list: {insertion_sort(unsorted_list, constants)}
    Initial list: {temp_list}
    """
    )


def show_insertion_sort_animation_with_constants(constants):
    """
    Tests the merge sort algorithm with the constants dictionary
    """
    sort_algorithm_name = "INSERTION SORT"
    unsorted_list = generate_unsorted_list_from_constants(constants, sort_algorithm_name)
    temp_list = unsorted_list.copy()
    print(
        f"""
    To compare:
    Sorted list: {insertion_sort_animation(unsorted_list, constants)}
    Initial list: {temp_list}
    """
    )


def show_bubble_sort_with_constants(constants):
    """
    Tests the merge sort algorithm with the constants dictionary
    """
    sort_algorithm_name = "BUBBLE SORT"
    unsorted_list = generate_unsorted_list_from_constants(constants, sort_algorithm_name)
    temp_list = unsorted_list.copy()
    print(
        f"""
    To compare:
    Sorted list: {bubble_sort(unsorted_list, constants)}
    Initial list: {temp_list}
    """
    )


def show_bubble_sort_animation_with_constants(constants):
    """
    Tests the merge sort algorithm with the constants dictionary
    """
    sort_algorithm_name = "BUBBLE SORT"
    unsorted_list = generate_unsorted_list_from_constants(constants, sort_algorithm_name)
    temp_list = unsorted_list.copy()
    print(
        f"""
    To compare:
    Sorted list: {bubble_sort_animation(unsorted_list, constants)}
    Initial list: {temp_list}
    """
    )


def show_quick_sort_with_constants(constants):
    """
    Tests the merge sort algorithm with the constants dictionary
    """
    sort_algorithm_name = "QUICK SORT"
    unsorted_list = generate_unsorted_list_from_constants(constants, sort_algorithm_name)
    temp_list = unsorted_list.copy()
    resulted_list = quick_sort(unsorted_list, constants, temp_list)
    print("Final list: ")
    print_items(resulted_list, constants)
    print(
        f"""

    To compare:
    Sorted list: {resulted_list}
    Initial list: {temp_list}
    """
    )


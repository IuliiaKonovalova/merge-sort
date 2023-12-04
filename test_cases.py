import random
from merge_sort import merge_sort
from selection_sort import selection_sort
from print_sorted_key import print_sorted_keys
from animations.merge_sort_animation.merge_sort import *
from insertion_sort import insertion_sort


def generate_unsorted_list_from_constants(constants):
    """
    Generates an unsorted list of numbers
    :return: an unsorted list of numbers
    """
    unsorted_list = []
    for key in constants:
        unsorted_list.append(key)
    random.shuffle(unsorted_list)
    print_sorted_keys(unsorted_list, constants)
    print("\n")
    print("!!!UNSORTED LIST: ", unsorted_list)
    return unsorted_list


def show_merge_sort_with_constants(constants):
    """
    Tests the merge sort algorithm with the constants dictionary
    """
    unsorted_list = generate_unsorted_list_from_constants(constants)
    print("Sorted list: ", merge_sort(unsorted_list, constants))


def show_merge_sort_animation_with_constants(constants):
    """
    Tests the merge sort algorithm with the constants dictionary
    """
    unsorted_list = generate_unsorted_list_from_constants(constants)
    print("Sorted list: ", merge_sort_animation(unsorted_list, constants))


def show_selection_sort_with_constants(constants):
    """
    Tests the merge sort algorithm with the constants dictionary
    """
    unsorted_list = generate_unsorted_list_from_constants(constants)
    print("Sorted list: ", selection_sort(unsorted_list, constants))

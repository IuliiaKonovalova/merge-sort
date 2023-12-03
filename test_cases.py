import random
from merge_sort import merge_sort
# from constant_dictionary import constants
from print_sorted_key import print_sorted_keys

def generate_unsorted_list_from_constants(constants):
    """
    Generates an unsorted list of numbers
    :return: an unsorted list of numbers
    """
    unsorted_list = []
    # add the keys from constants to the list
    for key in constants:
        unsorted_list.append(key)
    # shuffle the list
    random.shuffle(unsorted_list)
    # show only values by the keys
    # for key in unsorted_list:
    #     print(constants[key], end="")
    # print values in a line with a space
    print_sorted_keys(unsorted_list, constants)
    print("\n")
    print("!!!UNSORTED LIST: ", unsorted_list)
    return unsorted_list


def test_merge_sort_with_constants(constants):
    """
    Tests the merge sort algorithm with the constants dictionary
    """
    unsorted_list = generate_unsorted_list_from_constants(constants)
    print("Sorted list: ", unsorted_list)
    print("Sorted list: ", merge_sort(unsorted_list, constants))

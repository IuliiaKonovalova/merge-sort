import os
from time import sleep
from tools.painting_constants import *
from tools.print_items import *


def bubble_sort_animation(list_data, constants_1):
    """
    Sorts a list of numbers using bubble sort algorithm
    Args:
        initial_list (list): list of numbers
    Returns:
        initial_list (list): sorted list of numbers
    """
    for i in range(len(list_data) - 1):
        for j in range(len(list_data) - 1):
            animation_printing(list_data, constants_1, i, j)
            if list_data[j] > list_data[j + 1]:
                animation_printing(list_data, constants_1, i, j)
                list_data[j], list_data[
                    j + 1
                ] = list_data[j + 1], list_data[j]
                animation_printing(list_data, constants_1, i, j)
                os.system("clear")
                print("BUBBLE SORT")
                if list_data == sorted(list_data):
                    print("FINAL SORTED LIST: ", list_data)
                    print_items(list_data, constants_1)
    return list_data


def animation_printing(list_data, constants_1, i, j):
    """
    Prints the animation of bubble sort
    Args:
        initial_list (list): list of numbers
    Returns:
        initial_list (list): sorted list of numbers
    """
    os.system("clear")
    print("BUBBLE SORT")
    print_list_with_pointers(list_data, i, j)
    print_items(list_data, constants_1)
    sleep(0.9)


def print_list_with_pointers(list_data, i, j):
    """
    Prints the items in a list
    Args:
        keys (list): list of numbers
        constants_dict (dict): dictionary of constants
    Returns:
        None
    """
    print("[", end="")
    last_index = len(list_data) - 1
    for k in range(len(list_data)):
            if k != last_index:
                if k == i and i == j :
                    print(
                        f"""{b_forestgreen(str(list_data[k]))}{white}""",
                        end=", "
                    )
                elif k == i:
                    print(
                        f"""{term.on_lightgreen(
                          term.green(str(list_data[k]))
                        )}""",
                        end=", "
                    )
                elif k == j:
                    print(
                        f"""{b_dodgerblue2(str(list_data[k]))}{white}""",
                        end=", "
                    )
                elif k == j + 1:
                    print(
                        f"""{b_purple1(str(list_data[k]))}{white}""",
                        end=", "
                    )
                else:
                    print(list_data[k], end=", ")
            elif k == last_index:
                if k == i and i == j:
                    print(
                        f"""{b_forestgreen(str(list_data[k]))}{white}""",
                        end=""
                    )
                elif k == i:
                    print(
                        f"""{term.on_lightgreen(
                          term.green(str(list_data[k]))
                        )}""",
                        end=""
                    )
                elif k == j:
                    print(
                        f"""{b_dodgerblue2(str(list_data[k]))}{white}""",
                        end=""
                    )
                elif k == j + 1:
                    print(
                        f"""{b_purple1(str(list_data[k]))}{white}""",
                        end=""
                    )
                else:
                    print(list_data[k], end="")
    print("]")

import os
from time import sleep
from tools.colorama_constants import *
from tools.print_items import *


def bubble_sort_animation(unordered_list, constants_1):
    sleep(1.9)
    os.system("clear")
    print("BUBBLE SORT")
    for i in range(len(unordered_list) - 1):
        for j in range(len(unordered_list) - 1):
            if unordered_list[j] > unordered_list[j + 1]:
                unordered_list[j], unordered_list[
                    j + 1
                ] = unordered_list[j + 1], unordered_list[j]
                print_list_with_pointers(unordered_list, i, j)
                print_items(unordered_list, constants_1)
                sleep(0.9)
                os.system("clear")
                print("BUBBLE SORT")
                if unordered_list == sorted(unordered_list):
                    print_list_with_pointers(unordered_list, i, j)
                    print_items(unordered_list, constants_1)
    return unordered_list


def print_list_with_pointers(unordered_list, i, j):
    """
    Prints the items in a list
    Args:
        keys (list): list of numbers
        constants_dict (dict): dictionary of constants
    Returns:
        None
    """
    print("[", end="")
    last_index = len(unordered_list) - 1
    for k in range(len(unordered_list)):
            if k != last_index:
                if k == i and i == j :
                    print(
                        f"""{red}{unordered_list[k]}{white}""",
                        end=", "
                    )
                elif k == i:
                    print(
                        f"""{green}{unordered_list[k]}{white}""",
                        end=", "
                    )
                elif k == j:
                    print(
                        f"""{blue}{unordered_list[k]}{white}""",
                        end=", "
                    )
                elif k == j + 1:
                    print(
                        f"""{magenta}{unordered_list[k]}{white}""",
                        end=", "
                    )
                else:
                    print(unordered_list[k], end=", ")
            elif k == last_index:
                if k == i and i == j:
                    print(
                        f"""{red}{unordered_list[k]}{white}""",
                        end=""
                    )
                elif k == i:
                    print(
                        f"""{green}{unordered_list[k]}{white}""",
                        end=""
                    )
                elif k == j:
                    print(
                        f"""{blue}{unordered_list[k]}{white}""",
                        end=""
                    )
                elif k == j + 1:
                    print(
                        f"""{magenta}{unordered_list[k]}{white}""",
                        end=""
                    )
                else:
                    print(unordered_list[k], end="")
    print("]")

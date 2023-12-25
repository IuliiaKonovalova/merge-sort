import os
from time import sleep
from tools.print_items import *
from tools.painting_constants import *


def quick_sort(unsorted_list, constants, temp_list):
    """
    Sorts a list of numbers using quick sort algorithm, recursively
    Args:
        initial_list (list): list of numbers
        constants_dict (dict): dictionary of constants
        temp_list (list): list of numbers
    Returns:
        initial_list (list): sorted list of numbers
    """
    if temp_list == unsorted_list:
        os.system('clear')
        print(
          f"""{yellow}QUICK SORT STEP BY STEP{white}
          """
        )
        input("Press Press Enter to continue...")
    if len(unsorted_list) <= 1:
        return unsorted_list
    else:
        print("Entering quick sort")
        pivot = unsorted_list[0]
        print(f"""
{yellow}Pivot: {pivot}{white}
""")
        print_temp_item(pivot, unsorted_list, constants)
        sleep(0.9)
        if len(unsorted_list) > 0:
            print()
            print_list_with_pivot(unsorted_list, pivot, constants)
            if len(unsorted_list) != len(temp_list):
                print_items(unsorted_list, constants)
                print()
        less_than_pivot = [x for x in unsorted_list[1:] if x <= pivot]
        if len(less_than_pivot) > 0:
            print(
                f"""
Less than pivot: {green}{less_than_pivot}{white}"""
            )
            print_items(less_than_pivot, constants)
        else:
            print(
                f"""
Less than pivot: {yellow}{less_than_pivot}{white}"""
            )
        greater_than_pivot = [x for x in unsorted_list[1:] if x > pivot]
        if len(greater_than_pivot) > 0:
            sleep(0.9)
            print(
                f"""
Greater than pivot: {blue}{greater_than_pivot}{white}
"""
            )
            print_items(greater_than_pivot, constants)
        else:
            print(
                f"""
Greater than pivot: {blue}{greater_than_pivot}{white}
"""
            )
        sleep(0.9)
        print()
        print_list_to_merge(less_than_pivot, pivot, greater_than_pivot)
        merged_list = get_whole_list(
            less_than_pivot,
            pivot,
            greater_than_pivot
        )
        if len(merged_list) > 0:
            input("Press Enter to see the merged list")
            print("\nMERGED LIST: ", merged_list)
            print_items(merged_list, constants)
            print()
            input("Press Enter to continue...")
        return quick_sort(
            less_than_pivot, constants, temp_list
        ) + [pivot] + quick_sort(greater_than_pivot, constants, temp_list)


def print_list_with_pivot(unsorted_list, pivot):
    """
    Prints the items in a list
    Args:
        keys (list): list of numbers
        constants_dict (dict): dictionary of constants
    Returns:
        None
    """
    print("[", end="")
    last_index = len(unsorted_list) - 1
    for k in range(len(unsorted_list)):
            if k != last_index:
                if unsorted_list[k] == pivot:
                    print(
                        f"""{yellow}{unsorted_list[k]}{white}""",
                        end=", "
                    )
                else:
                    print(
                        f"""{unsorted_list[k]}""",
                        end=", "
                    )
            else:
                if unsorted_list[k] == pivot:
                    print(
                        f"""{yellow}{unsorted_list[k]}{white}""",
                        end=""
                    )
                else:
                    print(
                        f"""{unsorted_list[k]}""",
                        end=""
                    )
    print("]")


def get_whole_list(less_than_pivot, pivot, greater_than_pivot):
    """
    Gets the whole list
    Args:
        less_than_pivot (list): list of numbers less than the pivot
        pivot (int): the pivot
        greater_than_pivot (list): list of numbers greater than the pivot
    Returns:
        list: the whole list
    """
    new_list = []
    for i in less_than_pivot:
        new_list.append(i)
    new_list.append(pivot)
    for i in greater_than_pivot:
        new_list.append(i)
    return new_list


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

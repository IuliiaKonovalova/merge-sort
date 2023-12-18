import os
from time import sleep
from tools.print_items import *
from tools.painting_constants import *


def insertion_sort_animation(list_data, constants):
    """
    Sorts a list of numbers using insertion sort algorithm
    Args:
        initial_list (list): list of numbers
    Returns:
        initial_list (list): sorted list of numbers
    """
    for scan_index in range(1, len(list_data)):
        temp = list_data[scan_index]
        printing_animation(temp, list_data, constants, None, scan_index)
        min_index = scan_index
        printing_animation(temp, list_data, constants, min_index, scan_index)
        while min_index > 0 and temp < list_data[min_index - 1]:
            list_data[min_index] = list_data[min_index - 1]
            min_index -= 1
            list_data[min_index] = temp
            printing_animation(
                temp,
                list_data,
                constants,
                min_index,
                scan_index
            )
        printing_animation(temp, list_data, constants, min_index, scan_index)
        os.system('clear')
        print(
      f"""{yellow}INSERTION SORT ANIMATION{white}
          """
        )
        print("FINAL SORTED LIST: ", list_data)
        print_items(list_data, constants)
    return list_data


def printing_animation(temp, list_data, constants, min_index, scan_index):
    """
    Prints the animation of insertion sort
    Args:
        initial_list (list): list of numbers
    Returns:
        initial_list (list): sorted list of numbers
    """
    os.system('clear')
    print(
      f"""{yellow}INSERTION SORT ANIMATION{white}
          """
    )
    print("\n TEMP: ", temp)
    print_temp_item(temp, list_data, constants)
    print("\n LIST: ", end="")
    print_list_with_pointers(list_data, min_index, scan_index)
    print("\n Sorting...")
    print_items(list_data, constants)
    sleep(0.9)


def print_list_with_pointers(list_data, min_index, scan_index):
    """
    Prints the items in a list with color pointers
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
            if k == min_index and min_index == scan_index :
                print(
                    f"""{term.on_lightgreen(
                      term.green(str(list_data[k]))
                    )}""",
                    end=", "
                )
            elif k == min_index:
                print(
                    f"""{b_yellow(str(list_data[k]))}{white}""",
                    end=", "
                )
            elif k == scan_index:
                print(
                    f"""{b_forestgreen(str(list_data[k]))}{white}""",
                    end=", "
                )
            else:
                print(
                    f"""{white}{list_data[k]}{white}""",
                    end=", "
                )
        else:
            if k == min_index and min_index == scan_index :
                print(
                    f"""{term.on_lightgreen(
                      term.green(str(list_data[k]))
                    )}""",
                    end=""
                )
            elif k == min_index:
                print(
                    f"""{b_yellow(str(list_data[k]))}{white}""",
                    end=""
                )
            elif k == scan_index:
                print(
                    f"""{b_forestgreen(str(list_data[k]))}{white}""",
                    end=""
                )
            else:
                print(
                    f"""{white}{list_data[k]}{white}""",
                    end=""
                )
    print("]")

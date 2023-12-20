import os
from time import sleep
from tools.print_items import *
from tools.painting_constants import *
from animations.insertion_sort_animation.printing_list_with_pointers import *


def animation_control(temp, list_data, constants, min_index, scan_index, in_progress):
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
    if in_progress:
        print("\n TEMP: ", temp)
        print_temp_item(temp, list_data, constants)
        print("\n LIST: ", end="")
        print_list_with_pointers(list_data, min_index, scan_index)
        print("\n Sorting...")
        print_items(list_data, constants)
    else:
        print("FINAL SORTED LIST: ", list_data)
        print("\n")
        print_items(list_data, constants)
    sleep(0.9)

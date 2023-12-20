import os
from time import sleep
from tools.painting_constants import *
from tools.print_items import *
from animations.bubble_sort_animation.printing_list_with_pointers import *


def animation_control(list_data, constants_1, i, j, in_progress):
    """
    Prints the animation of bubble sort
    Args:
        initial_list (list): list of numbers
    Returns:
        initial_list (list): sorted list of numbers
    """
    os.system("clear")
    print(
      f"""{yellow}BUBBLE SORT ANIMATION{white}
      """
    )
    if in_progress:
        print_list_with_pointers(list_data, i, j)
        print("\n")
        print_items(list_data, constants_1)
    else:
        print("FINAL SORTED LIST: ", list_data)
        print("\n")
        print_items(list_data, constants_1)
    sleep(0.5)

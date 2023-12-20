from animations.bubble_sort_animation.animation_control import *


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
            # printing animation
            animation_control(list_data, constants_1, i, j, in_progress=True)
            if list_data[j] > list_data[j + 1]:
                # printing animation
                animation_control(
                    list_data,
                    constants_1,
                    i,
                    j,
                    in_progress=True
                )
                list_data[j], list_data[
                    j + 1
                ] = list_data[j + 1], list_data[j]
                # printing animation
                animation_control(
                    list_data,
                    constants_1,
                    i,
                    j,
                    in_progress=True
                )
    if list_data == sorted(list_data):
        # printing animation
        animation_control(list_data, constants_1, i, j, in_progress=False)
    return list_data

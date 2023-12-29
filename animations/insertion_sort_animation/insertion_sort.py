from animations.insertion_sort_animation.animation_control import (
    animation_control
)


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
        animation_control(
            temp,
            list_data,
            constants,
            None,
            scan_index,
            in_progress=True
        )
        min_index = scan_index
        animation_control(
            temp, list_data, constants, min_index,
            scan_index,
            in_progress=True
        )
        while min_index > 0 and temp < list_data[min_index - 1]:
            list_data[min_index] = list_data[min_index - 1]
            min_index -= 1
            list_data[min_index] = temp
            animation_control(
                temp,
                list_data,
                constants,
                min_index,
                scan_index,
                in_progress=True
            )
        animation_control(
            temp,
            list_data,
            constants,
            min_index,
            scan_index,
            in_progress=True
        )
    animation_control(
        temp,
        list_data,
        constants,
        min_index,
        scan_index,
        in_progress=False
    )
    return list_data

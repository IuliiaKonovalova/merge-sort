def split_list(initial_list):
    """
    Splits a list into 2 parts
    Args:
        initial_list (list): list of numbers
    Returns:
        left_part (list): left part of the list
        right_part (list): right part of the list
    """
    mid_point = len(initial_list) // 2
    left_part = initial_list[:mid_point]
    right_part = initial_list[mid_point:]

    return left_part, right_part

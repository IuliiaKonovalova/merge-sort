from tools.print_items import print_items


def split_list(initial_list, constants):
    """
    Splits a list into 2 parts
    Args:
        initial_list (list): list of numbers
    Returns:
        left_part (list): left part of the list
        right_part (list): right part of the list
    """
    input("Enter split_list Press Enter to continue...")
    mid_point = len(initial_list) // 2
    print("\n MIDPOINT", mid_point)
    left_part = initial_list[:mid_point]
    print("\n LEFT: ", left_part)
    print_items(left_part, constants)
    right_part = initial_list[mid_point:]
    print("\n RIGHT: ", right_part)
    print_items(right_part, constants)
    return left_part, right_part

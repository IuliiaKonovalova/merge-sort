from constant_dictionary import constants


def split_list(initial_list):
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
    print("mid_point", mid_point)
    left_part = initial_list[:mid_point]
    print("left_part: ", left_part)
    for key in left_part:
        print(constants[key], end="")
    print("\n")
    right_part = initial_list[mid_point:]
    print("right_part: ", right_part)
    for key in right_part:
        print(constants[key], end="")
    print("\n")

    return left_part, right_part

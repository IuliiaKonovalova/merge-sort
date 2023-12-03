# from constant_dictionary import constants


def merge(left, right, constants):
    """
    Takes 2 lists and analyzes them to sort them in ascending order
    Args:
        left (list): list of numbers
        right (list): list of numbers
    Returns:
        sorted_list (list): list of numbers sorted in ascending order
    """
    input("Enter merge Press Enter to continue...")
    sorted_list = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    # append the remaining elements from left that was not fully iterated
    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    # append the remaining elements from right that was not fully iterated
    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    print("\nSORTED LIST: ", sorted_list)
    for key in sorted_list:
        print(constants[key], end="")
    print("\n")
    return sorted_list

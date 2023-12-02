def merge(left, list_2):
    """
    Takes 2 lists and analyzes them to sort them in ascending order
    Args:
        left (list): list of numbers
        right (list): list of numbers
    Returns:
        initial_sorted_list (list): list of numbers sorted in ascending order
    """
    initial_sorted_list = []
    i = 0
    j = 0
    # sort the list using i and j as pointers
    while i < len(left) and j < len(list_2):
        if left[i] < list_2[j]:
            initial_sorted_list.append(left[i])
            i += 1
        else:
            initial_sorted_list.append(list_2[j])
            j += 1
    # append the remaining elements from left that was not fully iterated
    while i < len(left):
        initial_sorted_list.append(left[i])
        i += 1
    # append the remaining elements from list_2 that was not fully iterated
    while j < len(list_2):
        initial_sorted_list.append(list_2[j])
        j += 1

    return initial_sorted_list

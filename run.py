def merge(list_1, list_2):
    """
    Takes 2 lists and anazlyzes them to sort them in ascending order
    Args:
        list_1 (list): list of numbers
        list_2 (list): list of numbers
    Returns:
        initial_sorted_list (list): list of numbers sorted in ascending order
    """
    initial_sorted_list = []
    i = 0
    j = 0
    # sort the list using i and j as pointers
    while i < len(list_1) and j < len(list_2):
        if list_1[i] < list_2[j]:
            initial_sorted_list.append(list_1[i])
            i += 1
        else:
            initial_sorted_list.append(list_2[j])
            j += 1
    # append the remaining elements from list_1 that was not fully iterated
    while i < list_1[i]:
        initial_sorted_list.append(list_1[i])
        i += 1
    # append the remaining elements from list_2 that was not fully iterated
    while j < list_2[j]:
        initial_sorted_list.append(list_2[j])
        j += 1

    return initial_sorted_list
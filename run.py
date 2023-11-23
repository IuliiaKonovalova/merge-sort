def merge(list_1, list_2):
    initial_sorted_list = []
    i = 0
    j = 0

    while i < len(list_1) and j < len(list_2):
        if list_1[i] < list_2[j]:
            initial_sorted_list.append(list_1[i])
            i += 1
        else:
            initial_sorted_list.append(list_2[j])
            j += 1

    while i < list_1[i]:
        initial_sorted_list.append(list_1[i])
        i += 1

    while j < list_2[j]:
        initial_sorted_list.append(list_2[j])
        j += 1

    return initial_sorted_list
def merge(list):
    initial_sorted_list = []
    i = 0
    j = 0

    while i < len(list) and j < len(list):
        if list[i] < list[j]:
            initial_sorted_list.append(list[i])
            i += 1
        else:
            initial_sorted_list.append(list[j])
            j += 1

    while i < list[i]:
        initial_sorted_list.append(list[i])
        i += 1

    while j < list[j]:
        initial_sorted_list.append(list[j])
        j += 1

    return initial_sorted_list
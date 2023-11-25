def split_list(initial_list):
    mid_point = initial_list // 2
    left_part = initial_list[:mid_point]
    right_part = initial_list[mid_point:]

    return left_part, right_part 
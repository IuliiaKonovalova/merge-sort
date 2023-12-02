from split_functionality import split_list
from merge_functionality import merge


def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    Takes O(kn log n) time
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split_list(list)
    print("left_half", left_half)
    print("right_half", right_half)
    left = merge_sort(left_half)
    print("left", left)
    right = merge_sort(right_half)
    print("right", right)

    return merge(left, right)
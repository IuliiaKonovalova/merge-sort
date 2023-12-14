import random
import time
import os
from tools.constant_dictionary import constants


# Function to print colored bars representing keys
def print_sorted_keys(keys):
    max_key = max(keys)
    for key in keys:
        normalized_key = int((key / max_key) * max_key)  # Normalizing key for bar length
        color_code = constants[key]
        print(color_code * normalized_key)

# get the length of constants
# length = len(constants)
# # get the keys_to_sort by creating shuffled list based on the length of constants
keys_to_sort1 = list(range(len(constants)))
keys_to_sort = random.sample(keys_to_sort1, len(keys_to_sort1))

# keys_to_sort = [3, 2, 1, 0]

# Visualize the sorting algorithm for the given list of keys
def merge_sort(keys):
    if len(keys) <= 1:
        return keys

    # Divide the list into halves and recursively sort each half
    mid = len(keys) // 2
    left_half = merge_sort(keys[:mid])
    right_half = merge_sort(keys[mid:])

    return merge(left_half, right_half)

# Merge sort implementation
def merge_sort(keys):
    if len(keys) <= 1:
        return keys

    # Divide the list into halves and recursively sort each half
    mid = len(keys) // 2
    left_half = merge_sort(keys[:mid])
    right_half = merge_sort(keys[mid:])

    return merge(left_half, right_half)

# Merge two sorted halves into a single sorted list
def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    visualize_merge_sort(result)
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

# Function to display each step of merge sort
def visualize_merge_sort(keys):
    # Clear terminal screen before printing the visualization
    os.system('clear')
    print_sorted_keys(keys)
    time.sleep(1)  # Add a delay for visualization

# Example list of keys (values to be sorted)
keys_to_sort = [9, 5, 7, 3, 11, 6, 2, 8]

# Visualize the sorting algorithm for the given list of keys (merge sort)
visualize_merge_sort(keys_to_sort)
sorted_keys = merge_sort(keys_to_sort.copy())
visualize_merge_sort(sorted_keys)
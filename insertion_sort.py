import os
import time
from tabulate import tabulate
from print_items import print_items


unordered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def insertion_sort(unordered_list):
    for scan_index in range(1, len(unordered_list)):
        temp = unordered_list[scan_index]
        min_index = scan_index
        while min_index > 0 and temp < unordered_list[min_index - 1]:
            unordered_list[min_index] = unordered_list[min_index - 1]
            min_index = min_index - 1
            unordered_list[min_index] = temp
    return unordered_list


# insertion_sort(unordered_list)



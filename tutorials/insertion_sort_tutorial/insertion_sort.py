import os
import time
from tools.print_items import print_items


def insertion_sort(list_data, constants):
    """
    Sorts a list of numbers using the insertion sort algorithm
    Args:
        list_data (list): list of numbers
        constants (dict): dictionary of constants
    Returns:
        list: sorted list of numbers
    """
    for scan_index in range(1, len(list_data)):
        print("SCAN_INDEX: ", scan_index)
        temp = list_data[scan_index]
        print("TEMP: ", temp)
        min_index = scan_index
        print("MIN_INDEX: ", min_index)
        while min_index > 0 and temp < list_data[min_index - 1]:
            list_data[min_index] = list_data[min_index - 1]
            print("ITEM AT MIN INDEX: ", list_data[min_index])
            min_index -= 1
            print("MIN_INDEX UPDATED: ", min_index)
            list_data[min_index] = temp
            print("ITEM AT MIN INDEX FROM TEMP: ", list_data[min_index])
        input("Enter Press Enter to continue...")
        os.system('clear')
        print("\n")
        print("LIST DATA AFTER SORT: ", list_data)
        print_items(list_data, constants)
        time.sleep(0.9)
    return list_data

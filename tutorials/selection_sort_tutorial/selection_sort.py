import time
import os
from tabulate import tabulate
from tools.print_items import print_items
from tools.constant_dictionary import *


def selection_sort(list_data, constants):
    """
    Sorts a list of numbers using selection sort algorithm
    Args:
        initial_list (list): list of numbers
    Returns:
        initial_list (list): sorted list of numbers
    """
    headers = ["scan_index", "1st POINTER", "2nd POINTER"]
    for scan_index in range(0, len(list_data)):
        table_data = []
        min_index = scan_index
        print("1st POINTER: ", min_index)
        for comp_index in range(scan_index + 1, len(list_data)):
            input("Enter Press Enter to continue...")
            os.system('clear')
            print("\n LIST DATA: ", list_data)
            print("2nd POINTER: ", comp_index)
            table_data.append([scan_index, min_index, comp_index])
            print(tabulate(table_data, headers=headers))
            if list_data[comp_index] < list_data[min_index]:
                min_index = comp_index
                input("Enter Press Enter to continue...")
                os.system('clear')
                print("\n LIST DATA: ", list_data)
                print("1st POINTER Update: ", min_index)
                table_data.append([scan_index, min_index, comp_index])
                print(tabulate(table_data, headers=headers))
        if min_index != scan_index:
            list_data[scan_index], list_data[min_index] = (
                list_data[min_index], list_data[scan_index]
            )
            print("\n")
            print("LIST DATA AFTER SORT: ", list_data)
            print_items(list_data, constants)
            table_data.append([scan_index, min_index, comp_index])
            print(tabulate(table_data, headers=headers))
            time.sleep(0.9)

    return list_data

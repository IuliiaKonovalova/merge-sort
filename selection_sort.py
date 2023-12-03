from print_sorted_key import print_sorted_keys
from test_cases import generate_unsorted_list_from_constants
from constant_dictionary import *


import time
import os

def selection_sort(list_data, constants):

    for scan_index in range(0, len(list_data)):
        min_index = scan_index
        print("1st POINTER: ", min_index)
        for comp_index in range(scan_index + 1, len(list_data)):
            print("2nd POINTER: ", comp_index)
            if list_data[comp_index] < list_data[min_index]:
                min_index = comp_index
                print("1st POINTER Update: ", min_index)
        if min_index != scan_index:
            list_data[scan_index], list_data[min_index] = list_data[min_index], list_data[scan_index]
            input("Enter Press Enter to continue...")
            os.system('clear')
            print("\n")
            print("LIST DATA AFTER SORT: ", list_data)
            print_sorted_keys(list_data, constants)
            time.sleep(0.9)

    return list_data

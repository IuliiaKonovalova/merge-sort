import time
import os
from print_items import print_items, print_temp_item
from constant_dictionary import *



def selection_sort_animation(list_data, constants):
    for scan_index in range(0, len(list_data)):
        min_index = scan_index
        print("!!SELECTION SORT ANIMATION")
        os.system('clear')
        print("SELECTION SORT ANIMATION")
        print("\n MIN_INDEX")
        print_temp_item(min_index, list_data, constants)
        print("\n")
        print("\n")
        print("LIST DATA AFTER SORT: ", list_data)
        print_items(list_data, constants)
        time.sleep(0.9)
        for comp_index in range(scan_index + 1, len(list_data)):
            if list_data[comp_index] < list_data[min_index]:
                min_index = comp_index
                os.system('clear')
                print("SELECTION SORT ANIMATION")
                print("\n MIN_INDEX")
                print_temp_item(min_index, list_data, constants)
                print("\n")
                print("LIST DATA AFTER SORT: ", list_data)
                print_items(list_data, constants)

        if min_index != scan_index:
            list_data[scan_index], list_data[min_index] = list_data[min_index], list_data[scan_index]
            os.system('clear')
            print("SELECTION SORT ANIMATION")
            print("\n MIN_INDEX")
            print_temp_item(min_index, list_data, constants)
            print("\n")
            print("LIST DATA AFTER SORT: ", list_data)
            print_items(list_data, constants)
            time.sleep(0.9)
    return list_data

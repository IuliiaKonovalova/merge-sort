from time import sleep
import os
from print_items import *
from colorama import Fore, Back, Style


def bubble_sort(unordered_list, constants):
    """
    Sorts a list of numbers using bubble sort algorithm
    Args:
        initial_list (list): list of numbers
    Returns:
        initial_list (list): sorted list of numbers
    """
    for i in range(len(unordered_list) - 1):
        print(f"""Index in i:  {Fore.GREEN}{i}{Fore.WHITE}""")
        for j in range(len(unordered_list) - 1):
            print(f"""Index in j:  {Fore.BLUE}{j}{Fore.WHITE}""")

            if unordered_list[j] > unordered_list[j + 1]:
                print_temp_item(unordered_list[j], unordered_list, constants)
                print_temp_item(unordered_list[j + 1], unordered_list, constants)

                unordered_list[j], unordered_list[
                    j + 1
                ] = unordered_list[j + 1], unordered_list[j]
                print("Swapping values")
                print_temp_item(unordered_list[j], unordered_list, constants)
                print_temp_item(unordered_list[j + 1], unordered_list, constants)
                print("\n")
                print("LIST now: ", unordered_list)
                print_items(unordered_list, constants)

    return unordered_list
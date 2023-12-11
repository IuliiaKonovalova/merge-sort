from print_items import *
from colorama import Fore


def quick_sort(unsorted_list, constants, temp_list):
    # temp_list
    if len(unsorted_list) <= 1:  # Base case: If the unsorted_listay has 0 or 1 element, it is already sorted
        return unsorted_list
    else:
        input("Press Press Enter to continue...")
        print("Entering quick sort")
        pivot = unsorted_list[0]  # Choosing the first element as the pivot
        print(f"""{Fore.GREEN}Pivot: {pivot}{Fore.WHITE}""")
        if len(unsorted_list) > 0:
            
            print_list_with_pivot(unsorted_list, pivot, constants)
            if len(unsorted_list) != len(temp_list):
                print_items(unsorted_list, constants)
                print()
            # print(f"""Less than pivot: {Fore.GREEN}{less_than_pivot}{Fore.WHITE}""")
        less_than_pivot = [x for x in unsorted_list[1:] if x <= pivot]  # Elements less than or equal to pivot
        if len(less_than_pivot) > 0:
            print(f"""Less than pivot: {Fore.YELLOW}{less_than_pivot}{Fore.WHITE}""")
            print_items(less_than_pivot, constants)
        else:
            print(f"""Less than pivot: {Fore.YELLOW}{less_than_pivot}{Fore.WHITE}""")
            # print("Empty")
        greater_than_pivot = [x for x in unsorted_list[1:] if x > pivot]  # Elements greater than pivot
        if len(greater_than_pivot) > 0:
            print(f"""Greater than pivot: {Fore.MAGENTA}{greater_than_pivot}{Fore.WHITE}""")
            print_items(greater_than_pivot, constants)
        else:
            print(f"""Greater than pivot: {Fore.MAGENTA}{greater_than_pivot}{Fore.WHITE}""")
        merged_list = get_whole_list(less_than_pivot, pivot, greater_than_pivot)
        if len(merged_list) > 0:
            input("Press Enter to see the merged list")
            print()
            print(f"""Merged list: {Fore.CYAN}{merged_list}{Fore.WHITE}""")
            print_items(merged_list, constants)
            print()
        # print_items(get_whole_list, constants)
        return quick_sort(less_than_pivot, constants, temp_list) + [pivot] + quick_sort(greater_than_pivot, constants, temp_list)


def print_list_with_pivot(unsorted_list, pivot, constants):
    """
    Prints the items in a list
    Args:
        keys (list): list of numbers
        constants_dict (dict): dictionary of constants
    Returns:
        None
    """
    print("[", end="")
    last_index = len(unsorted_list) - 1
    for k in range(len(unsorted_list)):
            if k != last_index:
                if unsorted_list[k] == pivot:
                    print(
                        f"""{Fore.GREEN}{unsorted_list[k]}{Fore.WHITE}""",
                        end=", "
                    )
                else:
                    print(
                        f"""{Fore.BLUE}{unsorted_list[k]}{Fore.WHITE}""",
                        end=", "
                    )
            else:
                if unsorted_list[k] == pivot:
                    print(
                        f"""{Fore.GREEN}{unsorted_list[k]}{Fore.WHITE}""",
                        end=""
                    )
                else:
                    print(
                        f"""{Fore.BLUE}{unsorted_list[k]}{Fore.WHITE}""",
                        end=""
                    )
    print("]")


def get_whole_list(less_than_pivot, pivot, greater_than_pivot):
    """
    Gets the whole list
    Args:
        less_than_pivot (list): list of numbers less than the pivot
        pivot (int): the pivot
        greater_than_pivot (list): list of numbers greater than the pivot
    Returns:
        list: the whole list
    """
    new_list = []
    for i in less_than_pivot:
        new_list.append(i)
    new_list.append(pivot)
    for i in greater_than_pivot:
        new_list.append(i)
    return new_list

from print_items import *
from colorama import Fore


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
            print_list_with_pointers(unordered_list, i, j)
            input("Enter Press Enter to continue...")
            if unordered_list[j] > unordered_list[j + 1]:
                print_temp_item(unordered_list[j], unordered_list, constants)
                print_temp_item(unordered_list[j + 1], unordered_list, constants)
                unordered_list[j], unordered_list[
                    j + 1
                ] = unordered_list[j + 1], unordered_list[j]
                print("Swapping values")
                print_temp_item(unordered_list[j], unordered_list, constants)
                print_temp_item(unordered_list[j + 1], unordered_list, constants)
                print("\nLIST now: ")
                print_list_with_pointers(unordered_list, i, j)
                print_items(unordered_list, constants)
                input("Enter Press Enter to continue...")
    return unordered_list


def print_list_with_pointers(unordered_list, i, j):
    print("[", end="")
    last_index = len(unordered_list) - 1
    for k in range(len(unordered_list)):
            if k != last_index:
                if k == i and i == j :
                    print(
                        f"""{Fore.RED}{unordered_list[k]}{Fore.WHITE}""",
                        end=", "
                    )
                elif k == i:
                    print(
                        f"""{Fore.GREEN}{unordered_list[k]}{Fore.WHITE}""",
                        end=", "
                    )
                elif k == j:
                    print(
                        f"""{Fore.BLUE}{unordered_list[k]}{Fore.WHITE}""",
                        end=", "
                    )
                elif k == j + 1:
                    print(
                        f"""{Fore.MAGENTA}{unordered_list[k]}{Fore.WHITE}""",
                        end=", "
                    )
                else:
                    print(unordered_list[k], end=", ")
            elif k == last_index:
                if k == i and i == j:
                    print(
                        f"""{Fore.RED}{unordered_list[k]}{Fore.WHITE}""",
                        end=""
                    )
                elif k == i:
                    print(
                        f"""{Fore.GREEN}{unordered_list[k]}{Fore.WHITE}""",
                        end=""
                    )
                elif k == j:
                    print(
                        f"""{Fore.BLUE}{unordered_list[k]}{Fore.WHITE}""",
                        end=""
                    )
                elif k == j + 1:
                    print(
                        f"""{Fore.MAGENTA}{unordered_list[k]}{Fore.WHITE}""",
                        end=""
                    )
                else:
                    print(unordered_list[k], end="")
    print("]")

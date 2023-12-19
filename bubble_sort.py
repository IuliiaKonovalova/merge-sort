from tools.print_items import *


def bubble_sort(unordered_list, constants):
    """
    Sorts a list of numbers using bubble sort algorithm
    Args:
        initial_list (list): list of numbers
    Returns:
        initial_list (list): sorted list of numbers
    """
    for i in range(len(unordered_list) - 1):
        print(f"""Index in i:  {green}{i}{white}""")
        for j in range(len(unordered_list) - 1):
            print(f"""Index in j:  {blue}{j}{white}""")
            print_list_with_pointers(unordered_list, i, j)
            input("Press Enter to continue...")
            if unordered_list[j] > unordered_list[j + 1]:
                print_temp_item(unordered_list[j], unordered_list, constants)
                print_temp_item(
                    unordered_list[j + 1],
                    unordered_list,
                    constants
                )
                unordered_list[j], unordered_list[
                    j + 1
                ] = unordered_list[j + 1], unordered_list[j]
                print("Swapping values")
                print_temp_item(unordered_list[j], unordered_list, constants)
                print_temp_item(
                    unordered_list[j + 1],
                    unordered_list,
                    constants
                )
                print("\nLIST now: ")
                print_list_with_pointers(unordered_list, i, j)
                print_items(unordered_list, constants)
                input("Press Enter to continue...")
    return unordered_list


def print_list_with_pointers(unordered_list, i, j):
    """
    Prints the items in a list
    Args:
        keys (list): list of numbers
        constants_dict (dict): dictionary of constants
    Returns:
        None
    """
    print("[", end="")
    last_index = len(unordered_list) - 1
    for k in range(len(unordered_list)):
            if k != last_index:
                if k == i and i == j :
                    print(
                        f"""{red}{unordered_list[k]}{white}""",
                        end=", "
                    )
                elif k == i:
                    print(
                        f"""{green}{unordered_list[k]}{white}""",
                        end=", "
                    )
                elif k == j:
                    print(
                        f"""{blue}{unordered_list[k]}{white}""",
                        end=", "
                    )
                elif k == j + 1:
                    print(
                        f"""{magenta}{unordered_list[k]}{white}""",
                        end=", "
                    )
                else:
                    print(unordered_list[k], end=", ")
            elif k == last_index:
                if k == i and i == j:
                    print(
                        f"""{red}{unordered_list[k]}{white}""",
                        end=""
                    )
                elif k == i:
                    print(
                        f"""{green}{unordered_list[k]}{white}""",
                        end=""
                    )
                elif k == j:
                    print(
                        f"""{blue}{unordered_list[k]}{white}""",
                        end=""
                    )
                elif k == j + 1:
                    print(
                        f"""{magenta}{unordered_list[k]}{white}""",
                        end=""
                    )
                else:
                    print(unordered_list[k], end="")
    print("]")

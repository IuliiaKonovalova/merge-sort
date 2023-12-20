from tools.painting_constants import *


def print_list_with_pointers(list_data, i, j):
    """
    Prints the items in a list
    Args:
        keys (list): list of numbers
        constants_dict (dict): dictionary of constants
    Returns:
        None
    """
    print("[", end="")
    last_index = len(list_data) - 1
    for k in range(len(list_data)):
            if k != last_index:
                if k == i and i == j :
                    print(
                        f"""{b_forestgreen(str(list_data[k]))}{white}""",
                        end=", "
                    )
                elif k == i:
                    print(
                        f"""{term.on_lightgreen(
                          term.green(str(list_data[k]))
                        )}""",
                        end=", "
                    )
                elif k == j:
                    print(
                        f"""{b_dodgerblue2(str(list_data[k]))}{white}""",
                        end=", "
                    )
                elif k == j + 1:
                    print(
                        f"""{b_purple1(str(list_data[k]))}{white}""",
                        end=", "
                    )
                else:
                    print(list_data[k], end=", ")
            elif k == last_index:
                if k == i and i == j:
                    print(
                        f"""{b_forestgreen(str(list_data[k]))}{white}""",
                        end=""
                    )
                elif k == i:
                    print(
                        f"""{term.on_lightgreen(
                          term.green(str(list_data[k]))
                        )}""",
                        end=""
                    )
                elif k == j:
                    print(
                        f"""{b_dodgerblue2(str(list_data[k]))}{white}""",
                        end=""
                    )
                elif k == j + 1:
                    print(
                        f"""{b_purple1(str(list_data[k]))}{white}""",
                        end=""
                    )
                else:
                    print(list_data[k], end="")
    print("]")

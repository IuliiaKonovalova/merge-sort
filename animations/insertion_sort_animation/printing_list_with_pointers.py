from tools.painting_constants import *


def print_list_with_pointers(list_data, min_index, scan_index):
    """
    Prints the items in a list with color pointers
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
            if k == min_index and min_index == scan_index :
                print(
                    f"""{term.on_lightgreen(
                      term.green(str(list_data[k]))
                    )}""",
                    end=", "
                )
            elif k == min_index:
                print(
                    f"""{b_yellow(str(list_data[k]))}{white}""",
                    end=", "
                )
            elif k == scan_index:
                print(
                    f"""{b_forestgreen(str(list_data[k]))}{white}""",
                    end=", "
                )
            else:
                print(
                    f"""{white}{list_data[k]}{white}""",
                    end=", "
                )
        else:
            if k == min_index and min_index == scan_index :
                print(
                    f"""{term.on_lightgreen(
                      term.green(str(list_data[k]))
                    )}""",
                    end=""
                )
            elif k == min_index:
                print(
                    f"""{b_yellow(str(list_data[k]))}{white}""",
                    end=""
                )
            elif k == scan_index:
                print(
                    f"""{b_forestgreen(str(list_data[k]))}{white}""",
                    end=""
                )
            else:
                print(
                    f"""{white}{list_data[k]}{white}""",
                    end=""
                )
    print("]")

from tools.painting_constants import *


def display_selection_sort_code():
    """
    Prints the code for the selection sort algorithm
    with colorama
    """
    print(
        f"""
{blue}def{white} selection_sort{yellow}({white}list_data, constants{yellow}){white}:
    {blue}for {white}scan_index in range{yellow}({white}0, len{yellow}({white}list_data{yellow})){white}:
        min_index = scan_index
        {blue}for{white} comp_index in range{yellow}({white}scan_index + 1, len{yellow}({white}list_data{yellow})){white}:
            {blue}if{white} list_data{yellow}[{white}comp_index{yellow}]{white} < list_data{yellow}[{white}min_index{yellow}]{white}:
                min_index = comp_index
        {blue}if{white} min_index != scan_index:
            list_data{yellow}[{white}scan_index{yellow}]{white}, list_data{yellow}[{white}min_index{yellow}]{white} = list_data{yellow}[{white}min_index{yellow}]{white}, list_data{yellow}[{white}scan_index{yellow}]{white}
    {blue}return{white} list_data
    """
    )

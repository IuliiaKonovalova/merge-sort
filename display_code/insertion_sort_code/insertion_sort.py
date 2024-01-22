from time import sleep
from tools.painting_constants import *
from menu_feature.back_menu_functionality import show_back_menu


def display_insertion_sort_code():
    """ Displays the code for the insertion sort algorithm """
    print(
        f"""
{blue}def{white} insertion_sort{yellow}({white}list_data{yellow}){white}:
    {blue}for{white} scan_index {blue}in{white} range{yellow}({white}1, len{yellow}({white}list_data{yellow})){white}:
        temp = list_data{yellow}[{white}scan_index{yellow}]{white}
        min_index = scan_index
        {blue}while{white} min_index > 0 {blue}and{white} temp < list_data{yellow}[{white}min_index - 1{yellow}]{white}:
            list_data{yellow}[{white}min_index{yellow}]{white} = list_data{yellow}[{white}min_index - 1{yellow}]{white}
            min_index -= 1
            list_data{yellow}[{white}min_index{yellow}]{white}] = temp
    {blue}return{white} list_data
    """
    )
    sleep(2)
    show_back_menu()

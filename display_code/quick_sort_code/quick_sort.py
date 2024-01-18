from time import sleep
from tools.painting_constants import *
from menu_feature.back_menu_functionality import show_back_menu


def display_quick_sort_code():
    """ Displays the code for the quick sort algorithm """
    print(
        f"""
{blue}def{white} quick_sort{yellow}({white}arr{yellow}){white}:
    {blue}if{white} len{yellow}({white}arr{yellow}){white} <= 1:
        {blue}return{white} arr
    {blue}else{white}:
        pivot = arr{yellow}[{white}0{yellow}]{white}
        less_than_pivot = {yellow}[{white}x for x in arr{yellow}[{white}1:{yellow}]{white} if x <= pivot{yellow}]{white}
        greater_than_pivot = {yellow}[{white}x for x in arr{yellow}[{white}1:{yellow}]{white} if x > pivot{yellow}]{white}
        {blue}return{white} quick_sort{yellow}({white}less_than_pivot{yellow}){white} + {yellow}[{white}pivot{yellow}]{white} + quick_sort{yellow}({white}greater_than_pivot{yellow}){white}
    """
    )
    sleep(2)
    show_back_menu()

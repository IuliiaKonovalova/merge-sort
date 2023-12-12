from tools.colorama_constants import *


def display_bubble_sort_code():
    """ Displays the code for the bubble sort algorithm """
    print(
        f"""
{blue}def{white} bubble_sort{yellow}({white}initial_list{yellow}){white}:
    {blue}for{white} i {blue}in{white} range{yellow}({white}len{yellow}({white}initial_list{yellow}){white} - 1{yellow}){white}:
        {blue}for{white} j {blue}in{white} range{yellow}({white}len{yellow}({white}initial_list{yellow}){white} - 1{yellow}){white}:
            {blue}if{white} initial_list{yellow}[{white}j{yellow}]{white} > initial_list{yellow}[{white}j + 1{yellow}]{white}:
                initial_list{yellow}[{white}j{yellow}]{white}, initial_list{yellow}[{white}j + 1{yellow}]{white} = initial_list{yellow}[{white}j + 1{yellow}]{white}, initial_list{yellow}[{white}j{yellow}]{white}
    {blue}return{white} initial_list
    """
    )

from time import sleep
from tools.painting_constants import *
from menu_feature.back_menu_functionality import show_back_menu


def display_merge_sort_code():
    """
    Prints the code for the merge sort algorithm
    with colorama
    """
    print(
        f"""
{blue}def {white}merge_sort_animation{yellow}({white}initial_list{yellow}){white}:

    {blue}if {white}len{yellow}({white}initial_list{yellow}){white} <= 1:
        {blue}return {white}initial_list
    left_half, right_half = split_list{yellow}({white}initial_list{yellow}){white}
    left = merge_sort_animation{yellow}({white}left_half{yellow}){white}
    right = merge_sort_animation{yellow}({white}right_half{yellow}){white}
    {blue}return{white} merge{yellow}({white}left, right{yellow}){white}
    """
    )

    sleep(2)
    print(
        f"""
{blue}def {white}split_list{yellow}({white}initial_list{yellow}){white}:
    mid_point = len{yellow}({white}initial_list{yellow}){white} // 2
    left_part = initial_list{yellow}[{white}:mid_point{yellow}]{white}
    right_part = initial_list{yellow}[{white}mid_point:{yellow}]{white}
    {blue}return{white} left_part, right_part
    """
    )

    sleep(2)
    print(
        f"""
{blue}def {white}merge{yellow}({white}left, right{yellow}){white}:
    sorted_list = {yellow}[]{white}
    i = 0
    j = 0
    {blue}while{white} i < len{yellow}({white}left{yellow}){white} and j < len{yellow}({white}right{yellow}){white}:
        {blue}if{white} left{yellow}[{white}i{yellow}]{white} < right{yellow}[{white}j{yellow}]{white}:
            sorted_list.append{yellow}({white}left{yellow}[{white}i{yellow}]{white}{yellow}){white}
            i += 1
        {blue}else{white}:
            sorted_list.append{yellow}({white}right{yellow}[{white}j{yellow}]{white}{yellow}){white}
            j += 1
    {green}# append the remaining elements from left that was not fully iterated{white}
    {blue}while{white} i < len{yellow}({white}left{yellow}){white}:
        sorted_list.append{yellow}({white}left{yellow}[{white}i{yellow}]{white}{yellow}){white}
        i += 1
    {green}# append the remaining elements from right that was not fully iterated{white}
    {blue}while{white} j < len{yellow}({white}right{yellow}){white}:
        sorted_list.append{yellow}({white}right{yellow}[{white}j{yellow}]{white}{yellow}){white}
        j += 1
    {blue}return{white} sorted_list
    """
    )
    sleep(2)
    show_back_menu()

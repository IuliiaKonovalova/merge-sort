from colorama import Fore
from time import sleep


def display_merge_sort_code():
    """
    Prints the code for the merge sort algorithm
    with colorama
    """
    print(
        f"""
{Fore.BLUE}def {Fore.WHITE}merge_sort_animation{Fore.YELLOW}({Fore.WHITE}initial_list{Fore.YELLOW}){Fore.WHITE}:

    {Fore.BLUE}if {Fore.WHITE}len{Fore.YELLOW}({Fore.WHITE}initial_list{Fore.YELLOW}){Fore.WHITE} <= 1:
        {Fore.BLUE}return {Fore.WHITE}initial_list
    left_half, right_half = split_list{Fore.YELLOW}({Fore.WHITE}initial_list{Fore.YELLOW}){Fore.WHITE}
    left = merge_sort_animation{Fore.YELLOW}({Fore.WHITE}left_half{Fore.YELLOW}){Fore.WHITE}
    right = merge_sort_animation{Fore.YELLOW}({Fore.WHITE}right_half{Fore.YELLOW}){Fore.WHITE}
    {Fore.BLUE}return{Fore.WHITE} merge{Fore.YELLOW}({Fore.WHITE}left, right{Fore.YELLOW}){Fore.WHITE}
    """
    )
    sleep(2)
    print(
        f"""
{Fore.BLUE}def {Fore.WHITE}split_list{Fore.YELLOW}({Fore.WHITE}initial_list{Fore.YELLOW}){Fore.WHITE}:
    mid_point = len{Fore.YELLOW}({Fore.WHITE}initial_list{Fore.YELLOW}){Fore.WHITE} // 2
    left_part = initial_list{Fore.YELLOW}[{Fore.WHITE}:mid_point{Fore.YELLOW}]{Fore.WHITE}
    right_part = initial_list{Fore.YELLOW}[{Fore.WHITE}mid_point:{Fore.YELLOW}]{Fore.WHITE}
    {Fore.BLUE}return{Fore.WHITE} left_part, right_part
    """
    )
    sleep(2)
    print(
        f"""
{Fore.BLUE}def {Fore.WHITE}merge{Fore.YELLOW}({Fore.WHITE}left, right{Fore.YELLOW}){Fore.WHITE}:
    sorted_list = {Fore.YELLOW}[]{Fore.WHITE}
    i = 0
    j = 0
    {Fore.BLUE}while{Fore.WHITE} i < len{Fore.YELLOW}({Fore.WHITE}left{Fore.YELLOW}){Fore.WHITE} and j < len{Fore.YELLOW}({Fore.WHITE}right{Fore.YELLOW}){Fore.WHITE}:
        {Fore.BLUE}if{Fore.WHITE} left{Fore.YELLOW}[{Fore.WHITE}i{Fore.YELLOW}]{Fore.WHITE} < right{Fore.YELLOW}[{Fore.WHITE}j{Fore.YELLOW}]{Fore.WHITE}:
            sorted_list.append{Fore.YELLOW}({Fore.WHITE}left{Fore.YELLOW}[{Fore.WHITE}i{Fore.YELLOW}]{Fore.WHITE}{Fore.YELLOW}){Fore.WHITE}
            i += 1
        {Fore.BLUE}else{Fore.WHITE}:
            sorted_list.append{Fore.YELLOW}({Fore.WHITE}right{Fore.YELLOW}[{Fore.WHITE}j{Fore.YELLOW}]{Fore.WHITE}{Fore.YELLOW}){Fore.WHITE}
            j += 1
    {Fore.GREEN}# append the remaining elements from left that was not fully iterated{Fore.WHITE}
    {Fore.BLUE}while{Fore.WHITE} i < len{Fore.YELLOW}({Fore.WHITE}left{Fore.YELLOW}){Fore.WHITE}:
        sorted_list.append{Fore.YELLOW}({Fore.WHITE}left{Fore.YELLOW}[{Fore.WHITE}i{Fore.YELLOW}]{Fore.WHITE}{Fore.YELLOW}){Fore.WHITE}
        i += 1
    {Fore.GREEN}# append the remaining elements from right that was not fully iterated{Fore.WHITE}
    {Fore.BLUE}while{Fore.WHITE} j < len{Fore.YELLOW}({Fore.WHITE}right{Fore.YELLOW}){Fore.WHITE}:
        sorted_list.append{Fore.YELLOW}({Fore.WHITE}right{Fore.YELLOW}[{Fore.WHITE}j{Fore.YELLOW}]{Fore.WHITE}{Fore.YELLOW}){Fore.WHITE}
        j += 1
    {Fore.BLUE}return{Fore.WHITE} sorted_list
    """
    )

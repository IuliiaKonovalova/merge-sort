from colorama import Fore


def display_quick_sort_code():
    print(
        f"""
{Fore.BLUE}def{Fore.WHITE} quick_sort{Fore.YELLOW}({Fore.WHITE}arr{Fore.YELLOW}){Fore.WHITE}:
    {Fore.BLUE}if{Fore.WHITE} len{Fore.YELLOW}({Fore.WHITE}arr{Fore.YELLOW}){Fore.WHITE} <= 1:
        {Fore.BLUE}return{Fore.WHITE} arr
    {Fore.BLUE}else{Fore.WHITE}:
        pivot = arr{Fore.YELLOW}[{Fore.WHITE}[0{Fore.YELLOW}]{Fore.WHITE}
        less_than_pivot = {Fore.YELLOW}[{Fore.WHITE}x for x in arr{Fore.YELLOW}[{Fore.WHITE}1:{Fore.YELLOW}]{Fore.WHITE} if x <= pivot{Fore.YELLOW}]{Fore.WHITE}
        greater_than_pivot = {Fore.YELLOW}[{Fore.WHITE}x for x in arr{Fore.YELLOW}[{Fore.WHITE}1:{Fore.YELLOW}]{Fore.WHITE} if x > pivot{Fore.YELLOW}]{Fore.WHITE}
        {Fore.BLUE}return{Fore.WHITE} quick_sort{Fore.YELLOW}({Fore.WHITE}less_than_pivot{Fore.YELLOW}){Fore.WHITE} + {Fore.YELLOW}[{Fore.WHITE}pivot{Fore.YELLOW}]{Fore.WHITE} + quick_sort{Fore.YELLOW}({Fore.WHITE}greater_than_pivot{Fore.YELLOW}){Fore.WHITE}
    """
    )
display_quick_sort_code()
from colorama import Fore


def display_bubble_sort_code():
    print(
        f"""
{Fore.BLUE}def{Fore.WHITE} bubble_sort{Fore.YELLOW}({Fore.WHITE}initial_list{Fore.YELLOW}){Fore.WHITE}:
    {Fore.BLUE}for{Fore.WHITE} i {Fore.BLUE}in{Fore.WHITE} range{Fore.YELLOW}({Fore.WHITE}len{Fore.YELLOW}({Fore.WHITE}initial_list{Fore.YELLOW}){Fore.WHITE} - 1{Fore.YELLOW}){Fore.WHITE}:
        {Fore.BLUE}for{Fore.WHITE} j {Fore.BLUE}in{Fore.WHITE} range{Fore.YELLOW}({Fore.WHITE}len{Fore.YELLOW}({Fore.WHITE}initial_list{Fore.YELLOW}){Fore.WHITE} - 1{Fore.YELLOW}){Fore.WHITE}:
            {Fore.BLUE}if{Fore.WHITE} initial_list{Fore.YELLOW}[{Fore.WHITE}j{Fore.YELLOW}]{Fore.WHITE} > initial_list{Fore.YELLOW}[{Fore.WHITE}j + 1{Fore.YELLOW}]{Fore.WHITE}:
                initial_list{Fore.YELLOW}[{Fore.WHITE}j{Fore.YELLOW}]{Fore.WHITE}, initial_list{Fore.YELLOW}[{Fore.WHITE}j + 1{Fore.YELLOW}]{Fore.WHITE} = initial_list{Fore.YELLOW}[{Fore.WHITE}j + 1{Fore.YELLOW}]{Fore.WHITE}, initial_list{Fore.YELLOW}[{Fore.WHITE}j{Fore.YELLOW}]{Fore.WHITE}
    {Fore.BLUE}return{Fore.WHITE} initial_list
    """
    )

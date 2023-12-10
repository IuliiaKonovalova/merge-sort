from colorama import Fore


def display_insertion_sort_code():
    print(
        f"""
{Fore.BLUE}def{Fore.WHITE} insertion_sort{Fore.YELLOW}({Fore.WHITE}list_data{Fore.YELLOW}){Fore.WHITE}:
    {Fore.BLUE}for{Fore.WHITE} scan_index {Fore.BLUE}in{Fore.WHITE} range{Fore.YELLOW}({Fore.WHITE}1, len{Fore.YELLOW}({Fore.WHITE}list_data{Fore.YELLOW})){Fore.WHITE}:
        temp = list_data{Fore.YELLOW}[{Fore.WHITE}scan_index{Fore.YELLOW}]{Fore.WHITE}
        min_index = scan_index
        {Fore.BLUE}while{Fore.WHITE} min_index > 0 {Fore.BLUE}and{Fore.WHITE} temp < list_data{Fore.YELLOW}[{Fore.WHITE}min_index - 1{Fore.YELLOW}]{Fore.WHITE}:
            list_data{Fore.YELLOW}[{Fore.WHITE}min_index{Fore.YELLOW}]{Fore.WHITE} = list_data{Fore.YELLOW}[{Fore.WHITE}min_index - 1{Fore.YELLOW}]{Fore.WHITE}
            min_index -= 1
            list_data{Fore.YELLOW}[{Fore.WHITE}min_index{Fore.YELLOW}]{Fore.WHITE}] = temp
    {Fore.BLUE}return{Fore.WHITE} list_data
    """
    )
display_insertion_sort_code()
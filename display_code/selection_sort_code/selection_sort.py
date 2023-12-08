from colorama import Fore


def display_selection_sort_code():
    print(
        f"""
{Fore.BLUE}def{Fore.WHITE} selection_sort{Fore.YELLOW}({Fore.WHITE}list_data, constants{Fore.YELLOW}){Fore.WHITE}:
    {Fore.BLUE}for {Fore.WHITE}scan_index in range{Fore.YELLOW}({Fore.WHITE}0, len{Fore.YELLOW}({Fore.WHITE}list_data{Fore.YELLOW})){Fore.WHITE}:
        min_index = scan_index
        {Fore.BLUE}for{Fore.WHITE} comp_index in range{Fore.YELLOW}({Fore.WHITE}scan_index + 1, len{Fore.YELLOW}({Fore.WHITE}list_data{Fore.YELLOW})){Fore.WHITE}:
            {Fore.BLUE}if{Fore.WHITE} list_data{Fore.YELLOW}[{Fore.WHITE}comp_index{Fore.YELLOW}]{Fore.WHITE} < list_data{Fore.YELLOW}[{Fore.WHITE}min_index{Fore.YELLOW}]{Fore.WHITE}:
                min_index = comp_index
        {Fore.BLUE}if{Fore.WHITE} min_index != scan_index:
            list_data{Fore.YELLOW}[{Fore.WHITE}scan_index{Fore.YELLOW}]{Fore.WHITE}, list_data{Fore.YELLOW}[{Fore.WHITE}min_index{Fore.YELLOW}]{Fore.WHITE} = list_data{Fore.YELLOW}[{Fore.WHITE}min_index{Fore.YELLOW}]{Fore.WHITE}, list_data{Fore.YELLOW}[{Fore.WHITE}scan_index{Fore.YELLOW}]{Fore.WHITE}
    {Fore.BLUE}return{Fore.WHITE} list_data
    """
    )

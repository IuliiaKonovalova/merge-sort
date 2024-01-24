from time import sleep
from menu_feature.back_menu_functionality import show_back_menu
from simple_term_menu import TerminalMenu
from menu_feature.menu_constants import *
from tools.constant_dictionary import *
from test_cases import show_bubble_sort_animation_with_constants, show_bubble_sort_with_constants, show_insertion_sort_animation_with_constants, show_insertion_sort_with_constants, show_merge_sort_animation_with_constants, show_merge_sort_with_constants, show_quick_sort_animation_with_constants, show_quick_sort_with_constants, show_selection_sort_animation_with_constants, show_selection_sort_with_constants
from display_code.merge_sort_code.merge_sort import display_merge_sort_code



list_length_options_menu = TerminalMenu(list_length_options)

def show_list_length_options_menu(algorithm_name, algorithm_option):
    """
    Displays the list length options menu
    Args:
        algorithm_name (str): name of the algorithm
        algorithm_option (str): option of the algorithm
    Returns:
        None
    """
    print(f"""{algorithm_name.upper()} - {algorithm_option.upper()}""")
    list_length_options_index = list_length_options_menu.show()
    list_length_options_choice = list_length_options[list_length_options_index]
    if algorithm_name == 'Merge Sort':
        if algorithm_option == 'animation':
            if list_length_options_choice == '1. Yellow to red':
                print(f'''YELLOW TO RED''')
                show_merge_sort_animation_with_constants(constants_1)
            elif list_length_options_choice == '2. Blue - White - Black':
                print(f'''SHORT VERSION''')
                show_merge_sort_animation_with_constants(constants_2)
            elif list_length_options_choice == '3. Full version':
                print(f'''FULL VERSION''')
                show_merge_sort_animation_with_constants(constants_3)
        elif algorithm_option == 'step by step':
            if list_length_options_choice == '1. Yellow to red':
                print(f'''YELLOW TO RED''')
                show_merge_sort_with_constants(constants_1)
            elif list_length_options_choice == '2. Blue - White - Black':
                print(f'''SHORT VERSION''')
                show_merge_sort_with_constants(constants_2)
            elif list_length_options_choice == '3. Full version':
                print(f'''FULL VERSION''')
                show_merge_sort_with_constants(constants_3)
        else:
            display_merge_sort_code()
    elif algorithm_name == 'Selection Sort':
        if algorithm_option == 'animation':
            if list_length_options_choice == '1. Yellow to red':
                print(f'''YELLOW TO RED''')
                show_selection_sort_animation_with_constants(constants_1)
            elif list_length_options_choice == '2. Blue - White - Black':
                print(f'''SHORT VERSION''')
                show_selection_sort_animation_with_constants(constants_2)
            elif list_length_options_choice == '3. Full version':
                print(f'''FULL VERSION''')
                show_selection_sort_animation_with_constants(constants_3)
        elif algorithm_option == 'step by step':
            if list_length_options_choice == '1. Yellow to red':
                print(f'''YELLOW TO RED''')
                show_selection_sort_with_constants(constants_1)
            elif list_length_options_choice == '2. Blue - White - Black':
                print(f'''SHORT VERSION''')
                show_selection_sort_with_constants(constants_2)
            elif list_length_options_choice == '3. Full version':
                print(f'''FULL VERSION''')
                show_selection_sort_with_constants(constants_3)
    elif algorithm_name == 'Insertion Sort':
        if algorithm_option == 'animation':
            if list_length_options_choice == '1. Yellow to red':
                print(f'''YELLOW TO RED''')
                show_insertion_sort_animation_with_constants(constants_1)
            elif list_length_options_choice == '2. Blue - White - Black':
                print(f'''SHORT VERSION''')
                show_insertion_sort_animation_with_constants(constants_2)
            elif list_length_options_choice == '3. Full version':
                print(f'''FULL VERSION''')
                show_insertion_sort_animation_with_constants(constants_3)
        elif algorithm_option == 'step by step':
            if list_length_options_choice == '1. Yellow to red':
                print(f'''YELLOW TO RED''')
                show_insertion_sort_with_constants(constants_1)
            elif list_length_options_choice == '2. Blue - White - Black':
                print(f'''SHORT VERSION''')
                show_insertion_sort_with_constants(constants_2)
            elif list_length_options_choice == '3. Full version':
                print(f'''FULL VERSION''')
                show_insertion_sort_with_constants(constants_3)
    elif algorithm_name == 'Quick Sort':
        if algorithm_option == 'animation':
            if list_length_options_choice == '1. Yellow to red':
                print(f'''YELLOW TO RED''')
                show_quick_sort_animation_with_constants(constants_1)
            elif list_length_options_choice == '2. Blue - White - Black':
                print(f'''SHORT VERSION''')
                show_quick_sort_animation_with_constants(constants_2)
            elif list_length_options_choice == '3. Full version':
                print(f'''FULL VERSION''')
                show_quick_sort_animation_with_constants(constants_3)
        elif algorithm_option == 'step by step':
            if list_length_options_choice == '1. Yellow to red':
                print(f'''YELLOW TO RED''')
                show_quick_sort_with_constants(constants_1)
            elif list_length_options_choice == '2. Blue - White - Black':
                print(f'''SHORT VERSION''')
                show_quick_sort_with_constants(constants_2)
            elif list_length_options_choice == '3. Full version':
                print(f'''FULL VERSION''')
                show_quick_sort_with_constants(constants_3)
    elif algorithm_name == 'Bubble Sort':
        if algorithm_option == 'animation':
            if list_length_options_choice == '1. Yellow to red':
                print(f'''YELLOW TO RED''')
                show_bubble_sort_animation_with_constants(constants_1)
            elif list_length_options_choice == '2. Blue - White - Black':
                print(f'''SHORT VERSION''')
                show_bubble_sort_animation_with_constants(constants_2)
            elif list_length_options_choice == '3. Full version':
                print(f'''FULL VERSION''')
                show_bubble_sort_animation_with_constants(constants_3)
        elif algorithm_option == 'step by step':
            if list_length_options_choice == '1. Yellow to red':
                print(f'''YELLOW TO RED''')
                show_bubble_sort_with_constants(constants_1)
            elif list_length_options_choice == '2. Blue - White - Black':
                print(f'''SHORT VERSION''')
                show_bubble_sort_with_constants(constants_2)
            elif list_length_options_choice == '3. Full version':
                print(f'''FULL VERSION''')
                show_bubble_sort_with_constants(constants_3)
    sleep(2)
    show_back_menu()
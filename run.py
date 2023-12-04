from simple_term_menu import TerminalMenu
from constant_dictionary import *
from test_cases import *
from display_code.merge_sort_code.merge_sort import *



def main():
    """
    Runs the merge sort algorithm implementation
    Asks user for a list of comma separated numbers
    """
    input("Press Enter to continue...")
    # let user input different numbers
    # numbers = input("Enter numbers separated by a comma: ")
    # convert string to list
    # numbers = string_to_list(numbers)
    # test_merge_sort(numbers)

    options = ['1. Merge Sort', '2. Selection Sort', '3. Insertion Sort', '4. Bubble Sort', '5. Quit']
    main_menu = TerminalMenu(options)
    algorithm_options = [
        '1. Animation',
        '2. Step by step',
        '3. Code',
    ]
    list_length_options = [
        '1. Yellow to red',
        '2. Short version',
        '3. Full version',
    ]
    algorithm_options_menu = TerminalMenu(algorithm_options)
    list_length_options_menu = TerminalMenu(list_length_options)
    quitting = False
    while quitting is not True:
        options_index = main_menu.show()
        options_choice = options[options_index]
        if options_choice == '5. Quit':
            print(f'''QUITTING...''')
            quitting = True
        elif options_choice == '1. Merge Sort':
            print(f'''MERGE SORT''')
            algorithm_options_index = algorithm_options_menu.show()
            algorithm_choice = algorithm_options[algorithm_options_index]
            if algorithm_choice == '1. Animation':
                list_length_options_index = list_length_options_menu.show()
                list_length_options_choice = list_length_options[list_length_options_index]
                print(f'''ANIMATION''')
                if list_length_options_choice == '1. Yellow to red':
                    print(f'''YELLOW TO RED''')
                    show_merge_sort_animation_with_constants(constants_1)
                elif list_length_options_choice == '2. Short version':
                    print(f'''SHORT VERSION''')
                    show_merge_sort_animation_with_constants(constants_2)
                elif list_length_options_choice == '3. Full version':
                    print(f'''FULL VERSION''')
                    show_merge_sort_animation_with_constants(constants_3)
            elif algorithm_choice == '2. Step by step':
                list_length_options_index = list_length_options_menu.show()
                list_length_options_choice = list_length_options[list_length_options_index]
                print(f'''STEP BY STEP''')
                if list_length_options_choice == '1. Yellow to red':
                    print(f'''YELLOW TO RED''')
                    show_merge_sort_with_constants(constants_1)
                elif list_length_options_choice == '2. Short version':
                    print(f'''SHORT VERSION''')
                    show_merge_sort_with_constants(constants_2)
                elif list_length_options_choice == '3. Full version':
                    print(f'''FULL VERSION''')
                    show_merge_sort_with_constants(constants_3)
            elif algorithm_choice == '3. Code':
                print(f'''CODE''')
                display_merge_sort_code()
        elif options_choice == '2. Selection Sort':
            print(f'''SELECTION SORT''')
            algorithm_options_index = algorithm_options_menu.show()
            algorithm_choice = algorithm_options[algorithm_options_index]
            if algorithm_choice == '1. Animation':
                list_length_options_index = list_length_options_menu.show()
                list_length_options_choice = list_length_options[list_length_options_index]
                print(f'''ANIMATION''')
                if list_length_options_choice == '1. Yellow to red':
                    print(f'''YELLOW TO RED''')
                    show_selection_sort_animation_with_constants(constants_1)
                elif list_length_options_choice == '2. Short version':
                    print(f'''SHORT VERSION''')
                    show_selection_sort_animation_with_constants(constants_2)
                elif list_length_options_choice == '3. Full version':
                    print(f'''FULL VERSION''')
                    show_selection_sort_animation_with_constants(constants_3)
            elif algorithm_choice == '2. Step by step':
                list_length_options_index = list_length_options_menu.show()
                list_length_options_choice = list_length_options[list_length_options_index]
                print(f'''STEP BY STEP''')
                if list_length_options_choice == '1. Yellow to red':
                    print(f'''YELLOW TO RED''')
                    show_selection_sort_with_constants(constants_1)
                elif list_length_options_choice == '2. Short version':
                    print(f'''SHORT VERSION''')
                    show_selection_sort_with_constants(constants_2)
                elif list_length_options_choice == '3. Full version':
                    print(f'''FULL VERSION''')
                    show_selection_sort_with_constants(constants_3)


if __name__ == "__main__":
    main()

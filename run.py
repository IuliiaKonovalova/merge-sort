from simple_term_menu import TerminalMenu
# from string_to_list import string_to_list
from constant_dictionary import *
from test_cases import *



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
    sub_options = [
        '1. "Yellow to red"',
        '2. "Short version"',
        '3. "Full version"',
    ]
    sub_menu = TerminalMenu(sub_options)
    quitting = False
    while quitting is not True:
        options_index = main_menu.show()
        options_choice = options[options_index]
        if options_choice == '5. Quit':
            print(f'''QUITTING...''')
            quitting = True
        elif options_choice == '1. Merge Sort':
            print(f'''MERGE SORT''')
            # test_merge_sort()
            sub_index = sub_menu.show()
            sub_choice = sub_options[sub_index]
            if sub_choice == '1. "Yellow to red"':
                print(f'''YELLOW TO RED''')
                show_merge_sort_with_constants(constants_1)
            elif sub_choice == '2. "Short version"':
                print(f'''SHORT VERSION''')
                show_merge_sort_with_constants(constants_2)
            elif sub_choice == '3. "Full version"':
                print(f'''FULL VERSION''')
                show_merge_sort_with_constants(constants_3)
        elif options_choice == '2. Selection Sort':
            print(f'''SELECTION SORT''')
        elif options_choice == '3. Insertion Sort':
            print(f'''INSERTION SORT''')
        elif options_choice == '4. Bubble Sort':
            print(f'''BUBBLE SORT''')

if __name__ == "__main__":
    main()

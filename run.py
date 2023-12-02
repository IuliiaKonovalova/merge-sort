from string_to_list import string_to_list
from test_cases import test_merge_sort


def main():
    """
    Runs the merge sort algorithm implementation
    Asks user for a list of comma separated numbers
    """
    input("Press Enter to continue...")
    # let user input different numbers
    numbers = input("Enter numbers separated by a comma: ")
    # convert string to list
    numbers = string_to_list(numbers)
    test_merge_sort(numbers)


if __name__ == "__main__":
    main()

def string_to_list(string):
    """
    Converts a string of comma separated numbers to a list of integers
    :param string: a string of comma separated numbers
    :return: a list of integers
    """
    input("Enter string_to_list Press Enter to continue...")
    # convert string to list
    numbers = string.split(",")
    # convert list of strings to list of integers
    numbers = [int(number) for number in numbers]
    return numbers

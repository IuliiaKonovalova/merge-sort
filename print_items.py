import random


def print_items(keys, constants_dict):
    max_key = max(keys)
    if max_key == 0:
        max_key = 1
    for key in keys:
        if key < 10:
            print(" ", end="")
        print(key, end=": ")
        normalized_key = int(((key + 1) / max_key) * max_key)
        color_code = constants_dict[key]
        print(color_code * normalized_key)


def print_temp_item(key, list_data, constants_dict):
    max_key = max(list_data)
    if key == 0:
        key = 1
    if key < 10:
        print(" ", end="")
    print(key, end=": ")
    normalized_key = int(((key + 1) / max_key) * max_key)
    print(constants_dict[key] * normalized_key)

import random
# from constant_dictionary import constants


def print_items(keys, constants_dict):
    max_key = max(keys)
    if max_key == 0:
        max_key = 1
    for key in keys:
        if key < 10:
            print(" ", end="")
        print(key, end=": ")
        normalized_key = int(((key + 1) / max_key) * max_key)
        # normalized_key = int((key / max_key) * (max_key + 5))  # Normalizing key for bar length
        color_code = constants_dict[key]
        print(color_code * normalized_key)

# keys_to_sort1 = list(range(len(constants)))
# keys_to_sort = random.sample(keys_to_sort1, len(keys_to_sort1))


# print one item based on the key
def print_temp_item(key, list_data, constants_dict):
    # get max key from constants_dict
    max_key = max(list_data)
    if key == 0:
        key = 1
    if key < 10:
        print(" ", end="")
    print(key, end=": ")
    normalized_key = int(((key + 1) / max_key) * max_key)
    print(constants_dict[key] * normalized_key)
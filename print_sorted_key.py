import random
# from constant_dictionary import constants


def print_sorted_keys(keys, constants_dict):
    max_key = max(keys)
    for key in keys:
        # normalized_key = int((key / max_key) * (max_key + 1))  # Normalizing key for bar length
        print(key, end=": ")
        normalized_key = int(((key + 1) / max_key) * 40)
        color_code = constants_dict[key]
        print(color_code * normalized_key)

# keys_to_sort1 = list(range(len(constants)))
# keys_to_sort = random.sample(keys_to_sort1, len(keys_to_sort1))
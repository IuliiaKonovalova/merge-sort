import random
import time
import os

from tools.constant_dictionary import constants_1


# Function to print colored bars representing keys
def print_sorted_keys(keys):
    max_key = max(keys)
    for key in keys:
        normalized_key = int((key / max_key) * max_key)  # Normalizing key for bar length
        color_code = constants_1[key]
        print(color_code * normalized_key)

# get the length of constants
# length = len(constants)
# # get the keys_to_sort by creating shuffled list based on the length of constants
keys_to_sort1 = list(range(len(constants_1)))
keys_to_sort = random.sample(keys_to_sort1, len(keys_to_sort1))

# keys_to_sort = [3, 2, 1, 0]

# Visualize the sorting algorithm for the given list of keys
for i in range(len(keys_to_sort)):
    # Sorting algorithm - for example, here we're using bubble sort
    for j in range(len(keys_to_sort) - i - 1):
        if keys_to_sort[j] > keys_to_sort[j + 1]:
            keys_to_sort[j], keys_to_sort[j + 1] = keys_to_sort[j + 1], keys_to_sort[j]
            
            # Clear terminal screen before printing the updated visualization
            os.system('clear')
            print_sorted_keys(keys_to_sort)
            time.sleep(0.1)  # Add a small delay to visualize each step

# Print the final sorted keys
print("\033[0mFinal sorted keys:")
print(keys_to_sort)
keys_to_sort1 = list(range(len(constants_1)))
print(keys_to_sort1)
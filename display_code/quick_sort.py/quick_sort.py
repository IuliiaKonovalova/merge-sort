

# Example usage:
# my_list = [12, 4, 5, 6, 7, 3, 1, 15]
# sorted_list = quick_sort(my_list)
# print(sorted_list)


def quick_sort(arr):
    if len(arr) <= 1:  # Base case: If the array has 0 or 1 element, it is already sorted
        return arr
    else:
        pivot = arr[0]  # Choosing the first element as the pivot
        less_than_pivot = [x for x in arr[1:] if x <= pivot]  # Elements less than or equal to pivot
        greater_than_pivot = [x for x in arr[1:] if x > pivot]  # Elements greater than pivot
        
        # Recursively apply quick sort to partitions and concatenate results
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Example usage:
my_list = [12, 4, 5, 6, 7, 3, 1, 15]
sorted_list = quick_sort(my_list)
print(sorted_list)

# 2. Implement a binary search on a sorted array of strings.

# In this implementation, the binary_search function takes a sorted array of strings (sorted_array) and a target string (target). 
# It performs binary search to find the index of the target string in the array. 
# The function returns the index if the target is found, otherwise -1.

def binary_search(sorted_array, target):
    """
    Perform binary search on a sorted array of strings.

    Parameters:
    - sorted_array: The sorted array of strings.
    - target: The string to search for.

    Returns:
    - The index of the target string if found, otherwise -1.
    """
    low, high = 0, len(sorted_array) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_element = sorted_array[mid]

        if mid_element == target:
            return mid
        elif mid_element < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage:
sorted_strings = ["apple", "banana", "grape", "orange", "pineapple", "watermelon"]
target_string = "orange"

result = binary_search(sorted_strings, target_string)

if result != -1:
    print(f"{target_string} found at index {result}.")
else:
    print(f"{target_string} not found in the array.")

# 9. Write a function to search for a given number in a nearly sorted array (elements are swapped)

# In this implementation, the search_in_almost_sorted function takes a nearly sorted array (arr) and a target number (target). 
# It modifies the binary search algorithm to handle the nearly sorted condition. 
# Specifically, it checks if the target is equal to the middle element, the element before the middle, 
# or the element after the middle. If any of these conditions is true, it returns the respective index.

# The example usage demonstrates searching for the target number 5 in the nearly sorted array [2, 4, 1, 3, 5, 6, 8, 7]. 
# You can replace almost_sorted_array and target_number with your own array and target number.

def search_in_almost_sorted(arr, target):
    """
    Search for a given number in a nearly sorted array.

    Parameters:
    - arr: The nearly sorted array.
    - target: The number to search for.

    Returns:
    - The index of the target if found, otherwise -1.
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        if mid - 1 >= low and arr[mid - 1] == target:
            return mid - 1

        if mid + 1 <= high and arr[mid + 1] == target:
            return mid + 1

        if arr[mid] > target:
            high = mid - 2
        else:
            low = mid + 2

    return -1

# Example usage:
almost_sorted_array = [2, 4, 1, 3, 5, 6, 8, 7]
target_number = 5

result = search_in_almost_sorted(almost_sorted_array, target_number)

if result != -1:
    print(f"The target number {target_number} is found at index {result}.")
else:
    print(f"The target number {target_number} is not found in the array.")

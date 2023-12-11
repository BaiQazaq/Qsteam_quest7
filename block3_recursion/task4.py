# 4. Write a recursive function for binary search.


# This function takes a sorted array, a target element, and the indices of the low and high bounds of the search range. 
# It returns the index of the target element if found, or -1 if the element is not present in the array. 
# The function divides the search range in half with each recursive call, making it efficient for sorted arrays.

def binary_search_recursive(arr, target, low, high):
    """
    Perform binary search on a sorted array recursively.

    Parameters:
    - arr: The sorted array to be searched.
    - target: The element to be searched for.
    - low: The lower index of the search range.
    - high: The upper index of the search range.

    Returns:
    - The index of the target element if found, otherwise -1.
    """
    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Found the target element
        elif arr[mid] < target:
            # Search the right half
            return binary_search_recursive(arr, target, mid + 1, high)
        else:
            # Search the left half
            return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return -1  # Target element is not in the array

# Example usage:
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_element = 7

result = binary_search_recursive(sorted_array, target_element, 0, len(sorted_array) - 1)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the array.")

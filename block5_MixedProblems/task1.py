# 1. Sort a list of numbers using recursion.

# In this implementation, the merge_sort function recursively divides the list into two halves until each sublist has only 
# one element. It then merges the sorted sublists back together in a sorted manner.

# This example modifies the input list in-place. If you want to create a new sorted list without modifying the original, 
# you can modify the function to return a new list.

def merge_sort(arr):
    """
    Sort a list of numbers using the Merge Sort algorithm.

    Parameters:
    - arr: The list of numbers to be sorted.

    Returns:
    - The sorted list.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort the two halves
        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage:
numbers = [12, 4, 5, 6, 7, 3, 1, 15]
merge_sort(numbers)
print("Sorted numbers:", numbers)

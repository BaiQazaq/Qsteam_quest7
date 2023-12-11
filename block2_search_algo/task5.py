# 5. Write a program to find the first occurrence of an element in a sorted array using binary search

def binary_search_first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1  # Variable to store the index of the first occurrence

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            result = mid
            high = mid - 1  # Continue searching in the left half for the first occurrence
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result

# Example usage:
sorted_array = [1, 2, 2, 4, 4, 4, 7, 8, 9]
target_element = 4

first_occurrence_index = binary_search_first_occurrence(sorted_array, target_element)

if first_occurrence_index != -1:
    print(f"The first occurrence of {target_element} is at index {first_occurrence_index}.")
else:
    print(f"{target_element} is not present in the array.")

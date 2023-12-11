# 2. Write a program for binary search in a sorted array

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Target found, return the index
        elif arr[mid] < target:
            low = mid + 1  # Discard the left half
        else:
            high = mid - 1  # Discard the right half

    return -1  # Target not found in the array

# Example usage:
sorted_array = [1, 2, 4, 5, 7, 9, 11]
target_value = 7
result = binary_search(sorted_array, target_value)

if result != -1:
    print(f"Target value {target_value} found at index {result}.")
else:
    print(f"Target value {target_value} not found in the array.")

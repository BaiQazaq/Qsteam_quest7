# 7. mplement exponential search

def binary_search(arr, low, high, target):
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # If the target is not found in the specified range

def exponential_search(arr, target):
    n = len(arr)

    # Find the range for binary search by doubling the index
    i = 1
    while i < n and arr[i] < target:
        i *= 2

    # Perform binary search within the found range
    return binary_search(arr, i // 2, min(i, n - 1), target)

# Example usage:
sorted_array = [1, 2, 4, 6, 9, 12, 15, 18, 21, 24]
target_element = 15

result = exponential_search(sorted_array, target_element)

if result != -1:
    print(f"{target_element} found at index {result}.")
else:
    print(f"{target_element} is not present in the array.")

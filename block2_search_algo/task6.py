# 6. Create an interpolation search algorithm

def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        # Calculate the probable position using interpolation formula
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1  # If the target is not found in the array

# Example usage:
sorted_array = [1, 2, 4, 6, 9, 12, 15, 18, 21, 24]
target_element = 15

result = interpolation_search(sorted_array, target_element)

if result != -1:
    print(f"{target_element} found at index {result}.")
else:
    print(f"{target_element} is not present in the array.")

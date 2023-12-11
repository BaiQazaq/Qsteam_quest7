# 5. Implement jump search algorithm

import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))

    prev, current = 0, step

    # Jumping ahead by fixed steps
    while current < n and arr[current] < target:
        prev = current
        current += step

    # Performing linear search in the smaller range
    for i in range(prev, min(current, n)):
        if arr[i] == target:
            return i  # Target found, return the index

    return -1  # Target not found in the array

# Example usage:
sorted_array = [1, 2, 4, 5, 7, 9, 11, 13, 15, 17]
target_value = 7
result = jump_search(sorted_array, target_value)

if result != -1:
    print(f"Target value {target_value} found at index {result}.")
else:
    print(f"Target value {target_value} not found in the array.")

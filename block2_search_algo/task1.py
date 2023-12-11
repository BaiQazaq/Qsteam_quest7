# 1. Implement linear search in Python.

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Example usage:
input_array = [4, 2, 7, 1, 9, 5, 2]
target_value = 7
result = linear_search(input_array, target_value)

if result != -1:
    print(f"Target value {target_value} found at index {result}.")
else:
    print(f"Target value {target_value} not found in the array.")

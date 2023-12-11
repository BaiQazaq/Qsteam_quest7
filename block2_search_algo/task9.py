# 9. Create a program to find the smallest and largest element in an unsorted array

def find_min_max(arr):
    if not arr:
        return None, None  # Return None for both min and max if the array is empty

    min_val = float('inf')  # Initialize min_val to positive infinity
    max_val = float('-inf')  # Initialize max_val to negative infinity

    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return min_val, max_val

# Example usage:
unsorted_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

min_element, max_element = find_min_max(unsorted_array)

print(f"The smallest element in the array is: {min_element}")
print(f"The largest element in the array is: {max_element}")

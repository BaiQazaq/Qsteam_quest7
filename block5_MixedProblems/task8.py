# 8. Implement a program to find the two elements in an array whose sum is closest to zero.

# In this implementation, the closest_to_zero_sum_pair function takes an array (arr) as input and sorts it. 
# It then uses two pointers (left and right) to iterate through the array and find the pair of elements whose sum is closest to zero.

# The example usage demonstrates finding the two elements in the array [1, 60, -10, 70, -80, 85] whose sum is closest to zero.
# You can replace input_array with your own array.

def closest_to_zero_sum_pair(arr):
    """
    Find the two elements in an array whose sum is closest to zero.

    Parameters:
    - arr: The input array.

    Returns:
    - A tuple containing the pair of elements.
    """
    n = len(arr)

    if n < 2:
        return None

    # Sort the array
    arr.sort()

    # Initialize variables to store the result
    min_sum = float('inf')
    result_pair = None

    left, right = 0, n - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        # Check if the current pair has a sum closer to zero
        if abs(current_sum) < abs(min_sum):
            min_sum = current_sum
            result_pair = (arr[left], arr[right])

        # Move pointers based on the comparison
        if current_sum < 0:
            left += 1
        else:
            right -= 1

    return result_pair

# Example usage:
input_array = [1, 60, -10, 70, -80, 85]
result = closest_to_zero_sum_pair(input_array)

print("Two elements with sum closest to zero:", result)

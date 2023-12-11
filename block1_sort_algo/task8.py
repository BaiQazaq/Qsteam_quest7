# 8. Write a radix sort algorithm

def radix_sort(arr):
    # Find the maximum number to determine the number of digits
    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # 10 possible digits (0 to 9)

    # Count the occurrences of each digit at the current place value
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Update the count array to store the cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array by placing elements in their sorted order
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the sorted elements back to the original array
    for i in range(n):
        arr[i] = output[i]

# Example usage:
input_array = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(input_array)
print("Sorted Array:", input_array)

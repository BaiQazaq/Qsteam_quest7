# 7. Implement a counting sort algorithm for a list of integers

def counting_sort(arr):
    # Find the maximum and minimum values in the input array
    max_value = max(arr)
    min_value = min(arr)

    # Create a count array to store the count of each element
    count_array = [0] * (max_value - min_value + 1)

    # Count the occurrences of each element in the input array
    for num in arr:
        count_array[num - min_value] += 1

    # Reconstruct the sorted array based on the count array
    sorted_array = []
    for i in range(len(count_array)):
        sorted_array.extend([i + min_value] * count_array[i])

    return sorted_array

# Example usage:
input_array = [4, 2, 7, 1, 9, 5, 2]
sorted_array = counting_sort(input_array)
print("Input Array:", input_array)
print("Sorted Array:", sorted_array)

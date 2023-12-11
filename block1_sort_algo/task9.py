# 9. Sort an array of integers in descending order using any sorting algorithm

def quicksort_desc(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        greater = [x for x in arr[1:] if x >= pivot]
        lesser = [x for x in arr[1:] if x < pivot]
        return quicksort_desc(greater) + [pivot] + quicksort_desc(lesser)

# Example usage:
input_array = [4, 2, 7, 1, 9, 5, 2]
sorted_array = quicksort_desc(input_array)
print("Input Array:", input_array)
print("Sorted Array (Descending):", sorted_array)

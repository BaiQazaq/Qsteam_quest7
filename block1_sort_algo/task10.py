# 10. Create a program to sort an array of floating-point numbers

def quicksort_float(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        greater = [x for x in arr[1:] if x >= pivot]
        lesser = [x for x in arr[1:] if x < pivot]
        return quicksort_float(lesser) + [pivot] + quicksort_float(greater)

# Example usage:
input_array = [4.2, 2.1, 7.5, 1.3, 9.8, 5.0, 2.7]
sorted_array = quicksort_float(input_array)
print("Input Array:", input_array)
print("Sorted Array:", sorted_array)

# 5. Write a program for quicksort

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

# Example usage
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = quicksort(my_list)

print("Sorted array:", sorted_list)

# 7. Create a program to implement bubble sort in descending order.

# In this implementation, the bubble_sort_descending function takes a list (arr) as input and 
# performs the bubble sort algorithm in descending order. It iterates through the list and compares adjacent elements, 
# swapping them if they are in the wrong order. This process is repeated until the entire list is sorted.

# The example usage demonstrates sorting a list of numbers in descending order using bubble sort. 
# You can replace input_list with your own list.

def bubble_sort_descending(arr):
    """
    Implement bubble sort in descending order.

    Parameters:
    - arr: The input list to be sorted.

    Returns:
    - The sorted list in descending order.
    """
    n = len(arr)

    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                # Swap the elements if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage:
input_list = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", input_list)

bubble_sort_descending(input_list)

print("Sorted list in descending order:", input_list)

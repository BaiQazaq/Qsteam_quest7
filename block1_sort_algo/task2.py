# 2. Write a program for selection sort.

def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i + 1, n):
            # print(f"j - {j}, {arr[j] < arr[min_index]} - {arr[j]} *** {arr[min_index]}")
            if arr[j] < arr[min_index]:
                # print("min_ndex = ", min_index, 'j = ', j)
                min_index = j
                

        # Swap the found minimum element with the first element
        # print(f"arr[{i}] - {arr[i]}, arr[{min_index}] - {arr[min_index]} = arr[{min_index}] - {arr[min_index]} arr[{i}] - {arr[i]}")
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
my_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(my_list)

print("Sorted array:", my_list)

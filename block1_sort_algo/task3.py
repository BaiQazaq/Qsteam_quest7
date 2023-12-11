# 3. Create an insertion sort algorithm.

def insertion_sort(arr):
    # Traverse through all array elements starting from the second element
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1] that are greater than key to one position ahead of their current position
        j = i - 1
        print(f"Key - {key} j - {j}")
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            print(f"arr{j + 1} - {arr[j + 1]} ")
            j -= 1

        # Place the key at its correct position in the sorted array
        arr[j + 1] = key
        print(f'key - {key}')

# Example usage
my_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(my_list)

print("Sorted array:", my_list)

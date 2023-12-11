# 10. Implement a search algorithm to find the 'kth' smallest/largest element in an array

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, k):
    if low <= high:
        pivot_index = partition(arr, low, high)

        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index < k:
            return quickselect(arr, pivot_index + 1, high, k)
        else:
            return quickselect(arr, low, pivot_index - 1, k)

def find_kth_smallest(arr, k):
    if k > 0 and k <= len(arr):
        return quickselect(arr, 0, len(arr) - 1, k - 1)
    else:
        return None

# Example usage:
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
kth_smallest = 4

result = find_kth_smallest(array, kth_smallest)

if result is not None:
    print(f"The {kth_smallest}th smallest element in the array is: {result}")
else:
    print("Invalid value of k.")

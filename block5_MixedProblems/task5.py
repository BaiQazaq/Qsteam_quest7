# 5. Implement a program to find the intersection of two sorted arrays.

# In this implementation, find_intersection takes two sorted arrays (arr1 and arr2) and iterates through them simultaneously. 
# If the current elements in both arrays are equal, it adds the element to the intersection list. 
# If the element in arr1 is smaller, it moves to the next element in arr1, and if the element in arr2 is smaller, 
# it moves to the next element in arr2.

# The example usage demonstrates finding the intersection of two sorted arrays [1, 2, 4, 5, 6] and [2, 3, 5, 7]. 
# You can replace array1 and array2 with your own sorted arrays.

def find_intersection(arr1, arr2):
    """
    Find the intersection of two sorted arrays.

    Parameters:
    - arr1: The first sorted array.
    - arr2: The second sorted array.

    Returns:
    - A list representing the intersection of the two arrays.
    """
    intersection = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            intersection.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return intersection

# Example usage:
array1 = [1, 2, 4, 5, 6]
array2 = [2, 3, 5, 7]

result = find_intersection(array1, array2)
print(f"The intersection of {array1} and {array2} is: {result}")

# 8. Write a function to search for a given number in a 2D matrix

def search_in_2d_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1  # Start from the top-right corner

    while row < rows and col >= 0:
        current_element = matrix[row][col]

        if current_element == target:
            return True
        elif current_element < target:
            row += 1  # Move down if the current element is smaller than the target
        else:
            col -= 1  # Move left if the current element is larger than the target

    return False  # If the target is not found in the matrix

# Example usage:
matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17]
]

target_number = 9

if search_in_2d_matrix(matrix, target_number):
    print(f"{target_number} is present in the matrix.")
else:
    print(f"{target_number} is not present in the matrix.")

# 3. Create a function to perform a binary search on a list of strings

def binary_search_strings(string_list, target):
    low, high = 0, len(string_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if string_list[mid] == target:
            return mid  # Target found, return the index
        elif string_list[mid] < target:
            low = mid + 1  # Discard the left half
        else:
            high = mid - 1  # Discard the right half

    return -1  # Target not found in the list

# Example usage:
sorted_string_list = ["apple", "banana", "orange", "strawberry", "watermelon"]
target_string = "orange"
result = binary_search_strings(sorted_string_list, target_string)

if result != -1:
    print(f"Target string '{target_string}' found at index {result}.")
else:
    print(f"Target string '{target_string}' not found in the list.")

# 6. Create a function to sort an array of strings alphabetically

def sort_strings_alphabetically(strings):
    return sorted(strings)

# Example usage
my_strings = ["apple", "orange", "banana", "grape"]
sorted_strings = sort_strings_alphabetically(my_strings)

print("Original strings:", my_strings)
print("Sorted strings:", sorted_strings)

print("*"*70)

def sort_strings_alphabetically_in_place(strings):
    strings.sort()

# Example usage
my_strings = ["apple", "orange", "banana", "grape"]
sort_strings_alphabetically_in_place(my_strings)

print("Sorted strings in-place:", my_strings)

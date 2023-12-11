# 6. Write a recursive function to print all the subsets of a given set.

# In this implementation, the print_subsets function takes an input set (arr) and a current subset (subset) 
# being formed (used in recursion). It prints the current subset when the set becomes empty (base case). 
# In each recursive call, it includes the current element in the subset and generates subsets, 
# and then it excludes the current element and generates subsets.

# The example usage demonstrates finding and printing all subsets of the set [1, 2, 3]. 
# You can replace input_set with your own set.

def print_subsets(arr, subset=[]):
    """
    Print all subsets of a given set using recursion.

    Parameters:
    - arr: The input set.
    - subset: The current subset being formed (used in recursion).

    Returns:
    - None (prints subsets directly).
    """
    if not arr:
        print(subset)
        return

    # Include the current element and generate subsets
    print_subsets(arr[1:], subset + [arr[0]])

    # Exclude the current element and generate subsets
    print_subsets(arr[1:], subset)

# Example usage:
input_set = [1, 2, 3]
print("Subsets of", input_set, "are:")
print_subsets(input_set)

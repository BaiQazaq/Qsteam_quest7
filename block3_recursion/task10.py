# # 10. Write a recursive program to generate all permutations of a string

# In this implementation, the generate_permutations function recursively generates permutations 
# by choosing each character as the first character and then recursively generating permutations for the remaining substring. 
# The base case is an empty string, for which the function returns a list containing an empty string.

# The example usage generates all permutations of the string "abc" and prints each permutation. 
# You can replace the example_string with any string for which you want to generate permutations. 
# Keep in mind that the number of permutations grows factorially with the length of the input string, 
# so be cautious with longer strings.

def generate_permutations(input_str):
    """
    Generate all permutations of a string using recursion.

    Parameters:
    - input_str: The string for which permutations are generated.

    Returns:
    - A list of all permutations of the input string.
    """
    # Base case: an empty string has only one permutation, which is the empty string
    if len(input_str) == 0:
        return [""]
    
    permutations = []

    for i in range(len(input_str)):
        # Choose the i-th character as the first character
        first_char = input_str[i]

        # Exclude the i-th character and generate permutations for the remaining substring
        rest_of_string = input_str[:i] + input_str[i + 1:]
        rest_permutations = generate_permutations(rest_of_string)

        # Append the first character to each permutation of the remaining substring
        for permutation in rest_permutations:
            permutations.append(first_char + permutation)

    return permutations

# Example usage:
example_string = "abc"
permutations_list = generate_permutations(example_string)

print(f"Permutations of '{example_string}':")
for permutation in permutations_list:
    print(permutation)

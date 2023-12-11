# 6. Create a recursive function to reverse a string.

# In this implementation, the reverse_string function recursively reverses the substring excluding 
# the first character and then appends the first character at the end. 
# The recursion continues until the length of the input string becomes 0, at which point the original string is completely reversed.

def reverse_string(input_str):
    """
    Reverse a string using recursion.

    Parameters:
    - input_str: The string to be reversed.

    Returns:
    - The reversed string.
    """
    if len(input_str) == 0:
        return input_str
    else:
        # Recursive step: reverse the substring excluding the first character,
        # then append the first character at the end.
        return reverse_string(input_str[1:]) + input_str[0]

# Example usage:
original_string = "Hello, World!"
reversed_string = reverse_string(original_string)

print(f"Original string: {original_string}")
print(f"Reversed string: {reversed_string}")


# Python also provides a built-in way to reverse a string using the slice notation:

original_string = "Hello, World!"
reversed_string = original_string[::-1]
print(f"Original string: {original_string}")
print(f"Reversed string: {reversed_string}")

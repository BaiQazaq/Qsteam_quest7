# 3. Create a recursive function to count the number of vowels in a string.

# In this implementation, the count_vowels_recursive function checks if the first character of the string is a vowel (ignoring case) and 
# then recursively calls itself with the remaining substring. The base case is an empty string, which has no vowels.

# The example usage demonstrates counting vowels in the string "Hello, World!". You can replace the input_string 
# with any string you'd like to count vowels in.

def count_vowels_recursive(s):
    """
    Count the number of vowels in a string using recursion.

    Parameters:
    - s: The input string.

    Returns:
    - The number of vowels in the string.
    """
    # Base case: an empty string has no vowels
    if not s:
        return 0
    else:
        # Check if the first character is a vowel
        is_vowel = s[0].lower() in {'a', 'e', 'i', 'o', 'u'}
        
        # Recursively count vowels in the remaining substring
        return is_vowel + count_vowels_recursive(s[1:])

# Example usage:
input_string = "Hello, World!"
result = count_vowels_recursive(input_string)

print(f"The number of vowels in '{input_string}' is: {result}")



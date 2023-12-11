# 4. Write a greedy algorithm to sort characters by their frequency in a string

# In this implementation, the frequency_sort function first counts the frequency of each character in 
# the input string using a dictionary (char_frequency). 
# It then sorts the characters in descending order based on their frequency. 
# Finally, it builds the result string by repeating each character according to its frequency.

# The example usage demonstrates sorting the string "tree" by character frequency. 
# You can replace the input_string with any string you'd like to sort in this manner.

def frequency_sort(s):
    """
    Sort characters in a string by their frequency using a greedy algorithm.

    Parameters:
    - s: The input string.

    Returns:
    - The string sorted by character frequency.
    """
    char_frequency = {}

    # Count the frequency of each character
    for char in s:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    # Sort characters based on frequency in descending order
    sorted_chars = sorted(char_frequency, key=lambda char: char_frequency[char], reverse=True)

    # Build the result string by repeating each character according to its frequency
    result = ''.join([char * char_frequency[char] for char in sorted_chars])

    return result

# Example usage:
input_string = "tree"
result = frequency_sort(input_string)

print(f"The string '{input_string}' sorted by character frequency is: {result}")

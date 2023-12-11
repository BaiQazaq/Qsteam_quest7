# 9. Create a recursive function to check if a word is a palindrome

# In this implementation, the is_palindrome function recursively checks whether a word is a palindrome. 
# The base case is when the word has one character or is empty, in which case it is considered a palindrome. 
# Otherwise, it compares the first and last characters of the word and recursively checks the substring without these characters.

# The example usage checks if the word "level" is a palindrome and prints the result. 
# You can replace the example_word with any word you'd like to check for palindromicity.

def is_palindrome(word):
    """
    Check if a word is a palindrome using recursion.

    Parameters:
    - word: The word to be checked.

    Returns:
    - True if the word is a palindrome, False otherwise.
    """
    # Base case: an empty string or a string with one character is a palindrome
    if len(word) <= 1:
        return True
    else:
        # Check if the first and last characters are the same
        if word[0] == word[-1]:
            # Recursively check the substring without the first and last characters
            return is_palindrome(word[1:-1])
        else:
            return False

# Example usage:
example_word = "level"
result = is_palindrome(example_word)

if result:
    print(f"{example_word} is a palindrome.")
else:
    print(f"{example_word} is not a palindrome.")

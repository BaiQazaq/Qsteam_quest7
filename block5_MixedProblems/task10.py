# # 10. Implement a recursive program to find the nth catalan number.

# In this implementation, the catalan_number_recursive function takes an index n and recursively calculates 
# the nth Catalan number using the formula. The base case is when n is 0, and the function returns 1.

# The example usage demonstrates finding the 5th Catalan number. 
# You can replace n with any non-negative integer to find the corresponding Catalan number. 
# Keep in mind that this recursive approach may become inefficient for large values of n due to repeated computations. 
# In such cases, dynamic programming or memoization techniques can be applied for optimization.

def catalan_number_recursive(n):
    """
    Find the nth Catalan number using recursion.

    Parameters:
    - n: The index of the desired Catalan number.

    Returns:
    - The nth Catalan number.
    """
    if n == 0:
        return 1
    else:
        return catalan_number_recursive(n - 1) * (2 * (2 * n - 1)) // (n + 1)

# Example usage:
n = 5
result = catalan_number_recursive(n)

print(f"The {n}-th Catalan number is: {result}")

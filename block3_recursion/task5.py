# 5. Implement a program to calculate the power of a number using recursion.

# In this program, the power function recursively calculates the power of a number by 
# multiplying the base with the result of raising the base to the reduced exponent (exponent - 1). 
# The recursion continues until the exponent becomes 0, at which point the function 
# returns 1 (since any number raised to the power of 0 is 1).

# Keep in mind that while recursion is a clear and concise way to express the power calculation, 
# it may not be the most efficient for very large exponents due to the potential for a large number of recursive calls. 
# In practice, iterative methods or more advanced algorithms may be used for better performance.

def power(base, exponent):
    """
    Calculate the power of a number using recursion.

    Parameters:
    - base: The base number.
    - exponent: The exponent to which the base is raised.

    Returns:
    - The result of base raised to the exponent.
    """
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

# Example usage:
base_number = 2
exponent_value = 3

result = power(base_number, exponent_value)
print(f"{base_number}^{exponent_value} = {result}")

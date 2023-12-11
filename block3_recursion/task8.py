# 8. Implement a recursive function to find the greatest common divisor (GCD) of two numbers

# In this implementation, the gcd function uses the Euclidean algorithm recursively. 
# The algorithm states that the GCD of two numbers a and b is the same as the GCD of b and a % b. 
# The recursion continues until b becomes 0, at which point the GCD is found, and the last non-zero remainder is the GCD.

# The example usage demonstrates finding the GCD of 48 and 18, and the result will be 6.

def gcd(a, b):
    """
    Find the greatest common divisor (GCD) of two numbers using recursion.

    Parameters:
    - a: The first number.
    - b: The second number.

    Returns:
    - The GCD of a and b.
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Example usage:
number1 = 48
number2 = 18

result = gcd(number1, number2)
print(f"The GCD of {number1} and {number2} is: {result}")

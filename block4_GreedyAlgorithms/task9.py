# # 9. Implement a greedy method for the Egyptian fraction problem.

# In this implementation, the greedy_egyptian_fraction function takes a numerator and a denominator as input and 
# returns a list of unit fractions representing the Egyptian fraction. The algorithm iteratively selects the 
# largest possible unit fraction (ceiling division is used to ensure that the selected fraction is at least 1/n) 
# until the remaining fraction becomes zero.

# Keep in mind that while the greedy algorithm provides a representation, it may not always produce the optimal or 
# the shortest Egyptian fraction representation for all input fractions. There are more sophisticated algorithms to 
# find optimal representations, but the greedy method is simple and often sufficient.

def greedy_egyptian_fraction(numerator, denominator):
    """
    Find the Egyptian fraction representation of a given fraction using a greedy algorithm.

    Parameters:
    - numerator: The numerator of the fraction.
    - denominator: The denominator of the fraction.

    Returns:
    - A list of unit fractions representing the Egyptian fraction.
    """
    egyptian_fractions = []

    while numerator != 0:
        unit_fraction_denominator = -(-denominator // numerator)  # Ceiling division
        egyptian_fractions.append(unit_fraction_denominator)

        numerator = numerator * unit_fraction_denominator - denominator
        denominator *= unit_fraction_denominator

    return egyptian_fractions

# Example usage:
numerator_example = 4
denominator_example = 7

result_example = greedy_egyptian_fraction(numerator_example, denominator_example)
print(f"Egyptian Fraction representation of {numerator_example}/{denominator_example}: {result_example}")

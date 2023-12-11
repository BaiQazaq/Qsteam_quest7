# # 2. Write a program to solve the fractional knapsack problem.

# In this implementation, the items are sorted based on their value-to-weight ratios in descending order. 
# The algorithm then iterates through the sorted items, selecting items as long as there is available capacity in the knapsack. 
# If the capacity is not sufficient for the whole item, a fraction of the item is taken.

# Keep in mind that the greedy algorithm used here might not always produce the optimal solution for all 
# sets of values and weights. The 0/1 knapsack problem is NP-hard, and for some instances, 
# a dynamic programming approach may be necessary to find the truly optimal solution.

def fractional_knapsack(value, weight, capacity):
    """
    Solve the fractional knapsack problem using a greedy algorithm.

    Parameters:
    - value: A list of values for the items.
    - weight: A list of weights for the items.
    - capacity: The maximum weight the knapsack can hold.

    Returns:
    - A list of tuples representing the selected items and the fractions taken.
    """
    # Create a list of tuples (value, weight, value/weight) for each item
    items = [(v, w, v / w) for v, w in zip(value, weight)]

    # Sort the items in descending order based on value per weight
    items.sort(key=lambda x: x[2], reverse=True)

    total_value = 0
    knapsack = []

    for v, w, vw_ratio in items:
        if capacity >= w:
            # Take the whole item if there is enough capacity
            knapsack.append((v, w, 1.0))
            total_value += v
            capacity -= w
        else:
            # Take a fraction of the item to fill the remaining capacity
            fraction = capacity / w
            knapsack.append((v, w, fraction))
            total_value += v * fraction
            break  # Stop the loop as the knapsack is full

    return knapsack, total_value

# Example usage:
values = [60, 100, 120]
weights = [10, 20, 30]
knapsack_capacity = 50

selected_items, total_value = fractional_knapsack(values, weights, knapsack_capacity)

print(f"Selected items and their fractions:")
for item in selected_items:
    print(f"Value: {item[0]}, Weight: {item[1]}, Fraction: {item[2]:.2f}")

print(f"Total value in the knapsack: {total_value}")

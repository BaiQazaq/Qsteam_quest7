# 4. Implement a greedy algorithm to find the minimum number of coins for a given value

# In this implementation, the min_coins function takes a target value and a list of coin denominations as input. 
# It iterates through the denominations in descending order, selecting the largest denomination that can be used 
# without exceeding the remaining value. It updates the remaining value and records the count of each selected coin.

# Keep in mind that while the greedy algorithm works for some sets of coin denominations, 
# it may not always produce the optimal solution for all possible sets of denominations. 
# In some cases, a dynamic programming approach may be necessary to find the truly optimal solution.

def min_coins(value, denominations):
    """
    Find the minimum number of coins needed to represent a given value using a greedy algorithm.

    Parameters:
    - value: The target value for which to find the minimum number of coins.
    - denominations: A list of coin denominations, assumed to be in descending order.

    Returns:
    - A dictionary representing the count of each coin denomination used.
    """
    coin_counts = {}

    for coin in denominations:
        # Determine the number of times the current coin can be used
        count = value // coin

        # Update the value and record the count if the coin is used
        if count > 0:
            coin_counts[coin] = count
            value -= count * coin

    return coin_counts

# Example usage:
target_value = 63
coin_denominations = [25, 10, 5, 1]  # US coin denominations

result = min_coins(target_value, coin_denominations)

print(f"Target value: {target_value}")
print("Selected coins:")
for coin, count in result.items():
    print(f"{count} coin(s) of {coin} cents")

# # 1. Implement a greedy algorithm for the coin change problem

# In this implementation, the greedy_coin_change function takes an amount and a list of coin denominations as input. 
# It iterates through the denominations in descending order and selects the largest denomination that can be used 
# without exceeding the remaining amount. It updates the remaining amount and records the count of each selected coin.

# Keep in mind that while the greedy algorithm works for some currency systems (like the U.S. coin system), 
# it may not always produce the optimal solution for all possible sets of coin denominations. 
# In some cases, a dynamic programming approach may be necessary to find the truly optimal solution.

def greedy_coin_change(amount, denominations):
    """
    Perform coin change using a greedy algorithm.

    Parameters:
    - amount: The amount for which to make change.
    - denominations: A list of coin denominations, sorted in descending order.

    Returns:
    - A dictionary representing the selected coins and their counts.
    """
    coin_counts = {}

    for coin in denominations:
        # Determine the number of times the current coin can be used
        count = amount // coin

        # Update the amount and record the count if the coin is used
        if count > 0:
            coin_counts[coin] = count
            amount -= count * coin

    return coin_counts

# Example usage:
amount_to_change = 63
coin_denominations = [25, 10, 5, 1]  # US coin denominations

result = greedy_coin_change(amount_to_change, coin_denominations)

print(f"Amount to change: {amount_to_change}")
print("Selected coins:")
for coin, count in result.items():
    print(f"{count} coin(s) of {coin} cents")

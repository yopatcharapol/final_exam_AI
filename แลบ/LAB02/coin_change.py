def greedy_coin_change(coins, target_amount):
    coins.sort(reverse=True)  # Sort coins in descending order

    result = []
    remaining_amount = target_amount

    for coin in coins:
        num_coins = remaining_amount // coin
        remaining_amount %= coin
        result.extend([coin] * num_coins)

    if remaining_amount == 0:
        return result
    else:
        # If it's not possible to make exact change, return an empty list or handle accordingly
        return []

# Example usage:
coins = [10, 5, 2, 1]
target_amount = 63

change = greedy_coin_change(coins, target_amount)
print(f"Greedy Coin Change for {target_amount} cents: {change}")
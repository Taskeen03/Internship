def coinChange(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)                
    return dp[amount] if dp[amount] != amount + 1 else -1

coins_input = [1, 2, 5]
amount_input = 11
result = coinChange(coins_input, amount_input)
print(result)  
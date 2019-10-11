def number_of_ways(coins, n):
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    for i in range(len(coins)):
        for j in range(1, n+1):
            if coins[i] <= j:
                dp[j] = dp[j] + dp[j-coins[i]]

    print(dp)


n = 13
coins = [1,2,4]
number_of_ways(coins, n)
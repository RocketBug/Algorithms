def binary_knapsack(wt, val, W):
    dp = [[0 for i in range((W+1))] for j in range(len(wt)+1)]

    for i in range(1, len(wt)+1):
        for w in range(1, (W+1)):
            if wt[i-1] <= w:
                dp[i][w] = max(val[i-1]+dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    print(dp[len(wt)][W])





wt = [1,1,1]
val = [10,20,30]
W = 2
binary_knapsack(wt, val, W)

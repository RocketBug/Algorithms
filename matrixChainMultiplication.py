def matrixChain(arr, size):
    dp = [[0 for i in range(size)] for j in range(size)]

    for L in range(1, size-1):
        for i in range(1, size-L):
            j = L+i
            min_val = 99999

            for k in range(i, j):
                q = dp[i][k] + dp[k+1][j] + (arr[i-1] * arr[k] * arr[j])
                if q < min_val:
                    min_val = q

            dp[i][j] = min_val

    print(dp[1][size-1])

arr = [1,2,3,4,5]
size = len(arr)
matrixChain(arr, size)
def longest_path(i, j, dp, mat, n):
    if (i<0 or i>=n) or (j<0 or j>=n):
        return 0

    if dp[i][j] != -1:
        return dp[i][j]
    
    (x,y,z,w) = (-99,-99,-99,-99)

    if j<(n-1) and ((mat[i][j]+1) == mat[i][j+1]):
        x = dp[i][j] = 1 + longest_path(i, j+1, dp, mat, n)

    if j>0 and ((mat[i][j]+1) == mat[i][j-1]):
        y = dp[i][j] = 1 + longest_path(i, j-1, dp, mat, n)

    if i>0 and ((mat[i][j]+1) == mat[i-1][j]):
        z = dp[i][j] = 1 + longest_path(i-1, j, dp, mat, n)

    if i<(n-1) and ((mat[i][j]+1) == mat[i+1][j]):
        w = dp[i][j] = 1 + longest_path(i+1, j, dp, mat, n)


    dp[i][j] = max(x, max(y, max(z, max(w, 1))))

    return dp[i][j]


def initial():
    n = 3
    
    result = 1

    mat = [
        [1,2,9],
        [5,3,8],
        [4,6,7]
    ]
    dp = [[-1 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            if dp[i][j] == -1:
                longest_path(i, j, dp, mat, n)

                result = max(result, dp[i][j])
                
    print(result)


initial()
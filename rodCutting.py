def cut_rod(p, n):
    dp = [0 for i in range(n+1)]
    dp[0] = 0
    for j in range(1,n+1):
        q = -99999
        for i in range(0, j):
            q = max(q, p[i]+dp[(j-i)-1])
        
        dp[j] = q
    
    print(dp)



p = [1,5,8,9]
n = 4

cut_rod(p, n)
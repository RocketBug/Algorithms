def LCS(X, Y, m, n):
    L = [[0 for i in range(n+1)] for j in range(m+1)]  
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i][j-1], L[i-1][j])
    
    printLCS(X, L, m, n)
    print(L[m][n])
    
def printLCS(X, L, m, n):
    (i,j) = (m, n)
    result = ""

    while i > -1 and j > -1:
        if L[i][j] > L[i][j-1] and L[i][j] > L[i-1][j]:
            result += X[i-1]
            i = i-1
            j = j-1
                
                
        elif L[i][j] == L[i-1][j]:
            i = i-1

        elif L[i][j] == L[i][j-1]:
            j = j-1

    result = result[::-1]
    print(result)



Y = "AGGTAB"
X = "GXTXAYB"

LCS(X,Y,len(X), len(Y))
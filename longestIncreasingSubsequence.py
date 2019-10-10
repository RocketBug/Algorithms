def LIS(arr, n):
    lis = [1] * n

    (i,j,max_val) = (1,0,0)
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and lis[j] + 1 > lis[i]:
                lis[i] = lis[j] + 1

    for i in range(n):
        if max_val < lis[i]:
            max_val = lis[i]

    return max_val

arr = [10,22,9,33,21,50,41,60]
n = len(arr)
print(LIS(arr, n))

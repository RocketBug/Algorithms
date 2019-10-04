def mergeSort(A, left, right):
    if right - left <= 1:
        return A[left:right]

    if right - left > 1:
        mid = (right + left)//2
        Left = mergeSort(A, left, mid)
        Right = mergeSort(A, mid, right)

        return(merge(Left, Right))

def merge(L, R):
    (C, m, n) = ([], len(L), len(R))
    (i, j) = (0, 0)
    while (i+j) < (m+n):
        
        if i == m:
            C.append(R[j])
            j+=1

        elif j == n:
            C.append(L[i])
            i+=1

        elif L[i] <= R[j]:
            C.append(L[i])
            i+=1

        elif L[i] > R[j]:
            C.append(R[j])
            j+=1
    
    return C

list_a = list(range(0,1000000,2))
list_b = list(range(1,1000000,2))
list_c = list_a + list_b
mergeSort(list_c, 0, len(list_c))

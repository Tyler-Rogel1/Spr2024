def modQuicksort(A, low, high):
    if high-low <= 0:
        return A
    mid = (low+high)//2
    A[low],A[mid], = A[mid], A[low]
    # one pass of quicksort
    # left most of greater thans
    lmgt = low +1
    for i in range(low +1, high +1):
        if A[i]< A[low]:
            A[i], A[lmgt]=A[lmgt],A[i]
            lmgt += 1
    pivot = lmgt -1
    A[low], A[pivot] = A[pivot], A[low]
    modQuicksort(A, low, pivot-1)
    modQuicksort(A,pivot+1, high)

A = [3, 7, 2, 1, 6, 5,0,7]
print(modQuicksort(A, 0, len(A)-1))
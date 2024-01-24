def Quicksort(A, low, high):
    if high-low <= 0:
        return A



    # one pass of quicksort
    pivot_index = low
    # left most of greater thans
    lmgt = pivot_index
    for i in range(pivot_index +1, high +1):
        if A[i]< A[pivot_index]:
            A[i], A[lmgt]=A[lmgt],A[i]
            lmgt += 1
    rmlt = lmgt -1
    A[pivot_index], A[rmlt] = A[rmlt], A[pivot_index]
    Quicksort(A, low, rmlt-1)
    Quicksort(A,rmlt+1, high)

A = [3, 7, 2, 1, 6, 5,0,7]
Quicksort(A, 0, len(A)-1)
# Splits list into two, sorts the smaller lists, compares whats smaller between the two lists at the same index
# O = N * logN
def MergeSort(A):
    # if list is only one long, bail out and stop calling itself
    if len(A) <= 1:
        return
    # splits into two here
    mid = len(A)//2
    L= A[:mid]
    R= A[mid:]
    # magically sort L and R by calling itself
    MergeSort(L)
    MergeSort(R)
    # merge L and R back over A
    i = 0
    j = 0
    k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
        else:
            A[k] = R[i]
        i += 1
        j += 1
        k += 1 

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
    # merge L and R back over A
    i = 0
    j = 0
    k = 0
    # magically sort L and R by calling itself
    MergeSort(R)
    MergeSort(L)
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j += 1
        k += 1 
    
    while i < len(L):
        A[k] = L[i]
        i +=1
        k +=1
    while j < len(R):
        A[k] = R[j]
        j +=1
        k +=1 
A = [1,6,3,7,3,4,8,4]
MergeSort(A)
print(A)
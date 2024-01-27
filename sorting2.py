
import random
def CreateRandomList(size):
    return [random.randint(0, size-1) for i in range(size)]
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
A = CreateRandomList(10)
MergeSort(A)
print("Merge Sort: \n", A)

def Quicksort(A, low, high):
    if high-low <= 0:
        return 
    # one pass of quicksort
    # left most of greater thans
    lmgt = low +1
    for i in range(low +1, high +1):
        if A[i]< A[low]:
            A[i], A[lmgt]=A[lmgt],A[i]
            lmgt += 1
    pivot = lmgt -1
    A[low], A[pivot] = A[pivot], A[low]
    Quicksort(A, low, pivot-1)
    Quicksort(A,pivot+1, high)

A = CreateRandomList(10)
Quicksort(A, 0, len(A)-1)
print("Quicksort: \n", A)

def modQuicksort(A, low, high):
    if high-low <= 0:
        return 
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

A = CreateRandomList(10)
modQuicksort(A, 0, len(A)-1)
print("Modified Quicksort: \n", A)
# Measures number of compares vs problem size 
import random
class Counter:
    def __init__(self):
        self.count = 0
def CreateRandomList(size):
    return [random.randint(0, size-1) for i in range(size)]

def BubbleSort(A, c):
    changing = True
    while changing:
        changing = False
        for i in range(0, len(A)-1):
            c.count += 1
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                changing = True
    return A

def CountingSort(A):
    F=[0]*len(A)
    for v in A:
        F[v]+=1
    sorted_list = []
    for i in range(len(F)):
        num = i
        reps = F[i]
        for j in range(reps):
            sorted_list.append(num)
    return sorted_list


def QuicksortR(A, c, low, high):
    c.count +=1
    if high-low <= 0:
        return 
    # one pass of quicksort
    # left most of greater thans
    lmgt = low +1
    for i in range(low +1, high +1):
        c.count += 1
        if A[i]< A[low]:
            A[i], A[lmgt]=A[lmgt],A[i]
            lmgt += 1
    pivot = lmgt -1
    A[low], A[pivot] = A[pivot], A[low]
    QuicksortR(A, low, pivot-1)
    QuicksortR(A,pivot+1, high)

def Quicksort(A, c):
    QuicksortR(A,c,0,len(A)-1)

def main():
    sorts = [BubbleSort, ShakerSort, etc]
    for s in range(3,13):
        size = 2 ** s
        # Add formatted printing here
        print(s, end=" ")
        # loops over sorting algos
        for sort in sorts:
            A = CreateRandomList(size)
            B = A[:]
            # B[0], B[-1] = B[-1], B[0]
            B.sort()
            c = Counter()
            sort(A,c)
            print(c.count, end=" ")

# Measures number of compares vs problem size 
import random
import sys
import math
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

def CountingSort(A, c):
    c.count == len(A)
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


def QuicksortR(A, c, low, high, mod):
    if high-low <= 0:
        return 
    if mod:
        mid = (low+high)//2
        A[low],A[mid]=A[mid],A[low]
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
    QuicksortR(A,c,0,len(A)-1, False)
def ModQuicksort(A, c):
    QuicksortR(A,c,0,len(A)-1, True)

def main():
    sys.setrecursionlimit(5000)
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
            if c.count == 0:
                print("YIKES!!: count was 0")
                return
            print(math.log(c.count,2), end=" ")

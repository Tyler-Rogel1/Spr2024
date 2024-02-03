# Measures number of compares vs problem size 
import random
import math
import sys
class Counter:
    def __init__(self):
        self.count = 0

def CreateRandomList(size):
    return [random.randint(0, size-1) for i in range(size)]

def CreateMostlySortedList(size):
    sortedlist = sorted(CreateRandomList(size))
    sortedlist[0], sortedlist[-1] =  sortedlist[-1], sortedlist[0]
    return sortedlist

def Bubble(A, c):
    changing = True
    while changing:
        changing = False
        for i in range(0, len(A)-1):
            c.count += 1
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                changing = True
    return A

def Shaker(A, c):
    changing = True
    while changing:
        changing = False
        for i in range(0, len(A)-1):
            c.count += 1
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                changing = True
        for i in range(len(A)-1, 0, -1):
            c.count += 1
            if A[i] < A[i-1]:
                A[i], A[i-1] = A[i-1], A[i]
                changing = True
    return A

def Counting(A,c):
    c.count = len(A)
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

def Merge(A,c):
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
    Merge(R, c)
    Merge(L, c)
    while i < len(L) and j < len(R):
        c.count += 1
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
    QuicksortR(A,c, low, pivot-1)
    QuicksortR(A,c,pivot+1, high)

def Quick(A, c):
    QuicksortR(A,c,0,len(A)-1)


def MQuick(A, c):
    low = 0
    high = len(A)-1
    mid = (low+high)//2
    A[low],A[mid], = A[mid], A[low]
    Quick(A, c)

def Format(x):
    if x!=0:
        x = math.log(x)/math.log(2)
    return x

def main():
    sys.setrecursionlimit(5000)
    sorts = [Bubble, Shaker, Counting, Merge, Quick, MQuick]
    print("Counting compares on random data")
    print ("   ",end="")
    for sort in sorts:
        x = sort.__name__.ljust(9," ")
        print (x,end="")
    print()
    for s in range(3,13):
        size = 2 ** s
        # Add formatted printing here
        print("%02d" % (s), end=" ")
        # loops over sorting algos
        for sort in sorts:
            A = CreateRandomList(size)      
            c = Counter()
            sort(A,c)
            print("%05.2f" % (Format(c.count)), end="    ")
        print()
    print()    
    
    print("Counting compares on mostly sorted data")
    print ("   ",end="")
    for sort in sorts:
        x = sort.__name__.ljust(9," ")
        print (x,end="")
    print()
    for s in range(3,13):
        size = 2 ** s
        # Add formatted printing here
        print("%02d" % (s), end=" ")
        # loops over sorting algos
        for sort in sorts:
            A = CreateMostlySortedList(size)      
            c = Counter()
            sort(A,c)
            print("%05.2f" % (Format(c.count)), end="    ")
        print()

main()
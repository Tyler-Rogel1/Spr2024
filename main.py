# Tyler Rogel 2420 Sorting 1

import random
def CreateRandomList(size):
    return [random.randint(0, size-1) for i in range(size)]

def BubbleSort(A):
    changing = True
    while changing:
        changing = False
        for i in range(0, len(A)-1):
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

def ShakerSort(A):
    changing = True
    while changing:
        changing = False
        for i in range(0, len(A)-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                changing = True
        for i in range(len(A)-1, 0, -1):
            if A[i] < A[i-1]:
                A[i], A[i-1] = A[i-1], A[i]
                changing = True
    return A

def main():
    rand1 = CreateRandomList(10)
    print("random list: ", rand1)
    print("Bubble sorted list: ", BubbleSort(rand1))
    print()
    rand2 = CreateRandomList(10)
    print("random list: ", rand2)
    print("Shaker sorted list: ", ShakerSort(rand2))
    print()
    rand3 = CreateRandomList(10)
    print("random list: ", rand3)
    print("Counting sorted list: ", CountingSort(rand3))
main()
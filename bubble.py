def BubbleSort(A):
    changing = True
    while changing:
        changing = False
        for i in range(0, len(A)-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                changing = True
    return A

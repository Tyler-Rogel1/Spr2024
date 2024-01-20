def LinearSearch(A,x):
    for i in range(len(A)):
        if A[i]==x:
            return i
    return -1

list = [0,1,2,2,5,6,7,8,9,10]
print(LinearSearch(list, 3))
print(LinearSearch(list, 9))
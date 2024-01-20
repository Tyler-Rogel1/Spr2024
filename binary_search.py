def binarySearch(A,x):
    low = 0
    high = len(A)-1
    while high - low >=0:
        mid = (high + low)//2
        if A[mid]==x:
            return mid
        if x > A[mid]:
            low = mid+1
        if x < A[mid]:
            high = mid-1
    return -1
list = [0,1,2,2,2,5,6,7,8,9,10]
print(binarySearch(list, 3))
print(binarySearch(list, 9))
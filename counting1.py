# returns number of each value in the list
A = [7,0,5,0,1,2,2,4]
def countingSort(A):
    F=[0]*len(A)
    for v in A:
        F[v]+=1
    k=0 
    for i in range(len(F)):
        num = i
        reps = F[i]
        for i in range(reps):
            A[k] = num
            k+=1
    return F
print(countingSort(A))
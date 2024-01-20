#Returns sorted list  

A = [7,0,5,0,1,2,2,4]
def countingSort(A):
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
print(countingSort(A))
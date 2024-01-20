#Returns sorted list  
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

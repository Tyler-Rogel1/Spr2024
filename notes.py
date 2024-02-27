import random
# 2/26/24
# order N^2
def CreateRandomUniqueList(size):
    A = []
    while len(A) < size: #loop here
        r = random.randrange(0,size)
        if r not in A:
            A.append(r) #loop here
    return A
# order N
def CreateBagList(size):
    A = []
    bag = []
    for i in range(size): # loop here
        bag.append(i)
    for i in range(size): # loop here
        r = random.randrange(0, len(bag))
        A.append(bag[r])
        bag[r] = bag[-1]
        bag.pop()
    return A


# order N
def CreateTysonList(size):
    A = list(range(size)) 
    # random.shuffle(A)
    for i in range(size):
        r = random.randrange(0,size)
        A[i],A[r] = A[r],A[i]
    return A


print(CreateRandomUniqueList(10))
print(CreateBagList(10))
print(CreateTysonList(10))
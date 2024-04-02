import random
class Sheep:
    def __init__(self):
        self.alive=True
    
    def getAlive(self):
        return self.alive

class Node:
    def __init__(self, item):
        self.item = item
        self.nxt = None
class Container:
    def __init__(self):
        self.first = None

    def Insert(self,item):
        x = Node(item)
        x.nxt = self.first
        self.first = x
        return True

    def __iter__(self):
        current = self.first
        while current is not None:
            yield current.item
            current = current.nxt

    def Retrieve(self, item):
        current = self.first
        while current:
            if item == current.item:
                return current.item
            current = current.nxt
        return None



def main():
    # insert
    c = Container()
    for i in range(9):
        s = Sheep()
        c.Insert(s)

    # Traverse
    t1 = time.time()
    totalAge = 0
    for item in c:
        age = int(item.age)
        totalAge += age
    print("The average age is: ", totalAge/c.getSize())
    t2 = time.time()
    print("Total time for traverse is: ", (t2-t1))
    print()

    # Delete
    t3 = time.time()
    fin = open("Names/DeleteNames.txt", "r")
    for line in fin:
        ssn = line.strip()
        dummyStudent = Student("", "", ssn, "", "")
        ok = c.Delete(dummyStudent)
        if not ok:
            print("Couldn't delete: ", ssn," Because not in file")
    t4 = time.time()
    print("Total time for delete is: ", (t4-t3))
    print()
    fin.close()

    # Retrieve
    t5 = time.time()
    totalAge = 0
    size = 0
    fin = open("Names/RetrieveNames.txt", "r")
    for line in fin:
        ssn = line.strip()
        dummyStudent = Student("", "", ssn, "", "")
        s2 = c.Retrieve(dummyStudent)
        if s2 is not None:
            totalAge += int(s2.age)
            size += 1
        else:
            print("Couldn't retrieve: ", ssn," Because not in file")
    print("Average of retrieved ages is: ",  totalAge/size)
    t6 = time.time()
    print("Total time for retrieve is: ", (t6-t5))
    fin.close()
main()
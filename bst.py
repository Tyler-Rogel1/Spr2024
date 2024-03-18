import time
class Student:
    def __init__(self, first, last, ssn, email, age):
        self.first = first
        self.last = last
        self.ssn = ssn
        self.email = email
        self.age = age
    
    def __eq__(self, other):
        return self.ssn == other.ssn

class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def Insert(self,item):
        if self.Exists(item):
            return False
        else:
            n = Node(item)
            self.root = self.InsertR(n, self.root)
            return True
            
    def InsertR(self, n, current):
        if current is None:
            current = n
        elif n.item < current.item:
            current.left = self.InsertR(n, current.left)
        else:
            current.right = self.InsertR(n, current.right)
        return current
    def __iter__(self):
        current = self.first
        while current is not None:
            yield current.item
            current = current.nxt
        
    def getSize(self):
        return self.size

    def Size(self):
        current = self.first
        count = 0
        while current:
            count +=1 
            current = current.nxt
        return count
    def Exists(self,value):
        current = self.first
        while current:
            if current.item == value:
                return True
            current = current.nxt
        return False

    def Delete(self, item):
        if not self.Exists(item):
            return False
        if self.first.item == item:
            self.first = self.first.nxt
            self.size -= 1
            return True
            
        current = self.first
        while current.nxt.item != item:
            current = current.nxt
        current.nxt = current.nxt.nxt
        self.size -= 1
        return True
    def Retrieve(self, item):
        current = self.first
        while current:
            if item == current.item:
                return current.item
            current = current.nxt
        return None



def main():
    # insert
    c = BST()
    t1 = time.time()
    fin = open("Names/FakeNames.txt", "r")
    for line in fin:
        words = line.split()
        s = Student(words[0], words[1], words[2],words[3], words[4] )
        ok = c.Insert(s)
        if not ok:
            print("Student", words[0], words[1], "has duplicate ssn (", words[2],") not adding")
        
    t2 = time.time()
    print("total time for insert is: ", (t2-t1))
    print()
    fin.close()

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
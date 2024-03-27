# cs.usfca.edu/~galles/visualization/BTS.html
import time
class Student:
    def __init__(self, first, last, ssn, email, age):
        self.first = first
        self.last = last
        self.ssn = ssn
        self.email = email
        self.age = age
    
    def __eq__(self, other):
        if self.ssn == other.ssn:
            return True
        return False
    def __ne__(self, other):
        return self.ssn != other.ssn

    def __gt__(self, other):
        return self.ssn > other.ssn
    
    def __ge__(self, other):
        return self.ssn >= other.ssn
    
    def __lt__(self, other):
        return self.ssn < other.ssn
    
    def __le__(self, other):
        return self.ssn <= other.ssn

class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None

    def Insert(self,item):
        if self.Exists(item):
            return False
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
        yield from self.iterR(self.root)

    def iterR(self,current):
        if current is not None:
            yield from self.iterR(current.left)
            yield current.item
            yield from self.iterR(current.right)


    def Size(self):
        return self.sizeR(self.root)

    def sizeR(self, current):
        if current is None:
            return 0
        return 1 + self.sizeR(current.left) + self.sizeR(current.right)
    def Exists(self,value):
        return self.ExistsR(value, self.root)

    def ExistsR(self, item, current):
        if current is None:
            return False
        elif current.item == item:
            return True
        elif item < current.item:
            return self.ExistsR(item, current.left)
        elif item > current.item:
            return self.ExistsR(item, current.right)

    def Delete(self, item):
        if not self.Exists(item):
            return False
        self.root = self.DeleteR(item,self.root)
        return True

    def DeleteR(self, item, current):
        if item < current.item:
            current.left = self.DeleteR(item, current.left)
        elif item > current.item:
            current.right = self.DeleteR(item, current.right)
        else:
            if not current.left and not current.right: #Leaf case
                current = None
            elif not current.left and current.right: #One child right
                current = current.right
            elif current.left and not current.right: #one child left
                current = current.left
            else: # two child case
                S = current.right
                while S.left:
                    S = S.left
                current.item = S.item
                current.right = self.DeleteR(S.item, current.right)
        return current
            
        

    def Retrieve(self, item):
        return self.RetrieveR(item, self.root)
    
    def RetrieveR(self, item, current):
        if current is None:
            return None
        elif current.item == item:
            return current.item
        elif item < current.item:
            return self.RetrieveR(item, current.left)
        elif item > current.item:
            return self.RetrieveR(item, current.right)


def main():
    # insert
    c = BST()
    print("INSERT")
    t1 = time.time()
    fin = open("Names/FakeNamesMedium.txt", "r")
    insertfails = 0
    for line in fin:
        words = line.split()
        s = Student(words[0], words[1], words[2],words[3], words[4] )
        ok = c.Insert(s)
        if not ok:
            insertfails += 1
            # print("Student", words[0], words[1], "has duplicate ssn (", words[2],") not adding")
    print("Insert fails: ", insertfails)
        
    t2 = time.time()
    print("total time for insert is: ", (t2-t1))
    print()
    fin.close()

    # Traverse
    print("TRAVERSE")
    t1 = time.time()
    totalAge = 0
    for item in c:
        age = int(item.age)
        totalAge += age
    print("The average age is: ", totalAge/c.Size())
    t2 = time.time()
    print("Total time for traverse is: ", (t2-t1))
    print()

    # Delete
    print("DELETE")
    t3 = time.time()
    fin = open("Names/DeleteNamesMedium.txt", "r")
    dfails = 0
    for line in fin:
        ssn = line.strip()
        dummyStudent = Student("", "", ssn, "", "")
        ok = c.Delete(dummyStudent)
        if not ok:
            dfails += 1
            # print("Couldn't delete: ", ssn," Because not in file")
    print("Delete Fails: ", dfails)
    t4 = time.time()
    print("Total time for delete is: ", (t4-t3))
    print()
    fin.close()

    # Retrieve
    print("RETRIEVE")
    t5 = time.time()
    totalAge = 0
    size = 0
    fin = open("Names/RetrieveNamesMedium.txt", "r")
    rfails = 0
    for line in fin:
        ssn = line.strip()
        dummyStudent = Student("", "", ssn, "", "")
        s2 = c.Retrieve(dummyStudent)
        if s2 is not None:
            totalAge += int(s2.age)
            size += 1
        else:
            rfails += 1
            # print("Couldn't retrieve: ", ssn," Because not in file")
    print("Retrieve Fails:", rfails)
    print("Average of retrieved ages is: ",  totalAge/size)
    t6 = time.time()
    print("Total time for retrieve is: ", (t6-t5))
    fin.close()
main()
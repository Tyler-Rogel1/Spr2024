# cs.usfca.edu/~galles/visualization/BTS.html
import time
import math
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

    def __hash__(self):
        return int(self.ssn.replace("-",""))

class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

class Hash:
    def __init__(self, numItem):
        slots= 2*numItem +1
        while not isPrime(slots):
            slots +=2
        self.table = []
        for i in range(slots):
            self.table.append(None)

    def Exists(self,item):
        key = hash(item)
        index = key%len(self.table)
        while True:
            if self.table[index] is None:
                return False
            elif self.table[index] and self.table[index] == item:
                return True
            index +=1
            if index >= len(self.table):
                index = 0


    def Insert(self,item):
        if self.Exists(item):
            return False
        key = hash(item)
        index = key%len(self.table)
        while True:
            if self.table[index] is None or not self.table[index]:
                self.table[index] = item
                return True
            index +=1
            if index >= len(self.table):
                index = 0
        

    def __iter__(self):
        for item in self.table:
            if item is not None:
                yield item



    def Size(self):
        count = 0
        for item in self.table:
            if item is not None:
                count += 1
        return count
        

    def Delete(self, item):
        if not self.Exists(item):
            return False
        key = hash(item)
        index = key%len(self.table)
        while True:
            if self.table[index] is None:
                return False
            elif self.table[index] and self.table[index] == item:
                self.table[index] = False
                return True
            index +=1
            if index >= len(self.table):
                index = 0

           

    def Retrieve(self, item):
        key = hash(item)
        index = key%len(self.table)
        while True:
            if self.table[index] is None:
                return None
            elif self.table[index] and self.table[index] == item:
                return self.table[index]
            index +=1
            if index >= len(self.table):
                index = 0


def main():
    # insert
    c = Hash(600000)
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
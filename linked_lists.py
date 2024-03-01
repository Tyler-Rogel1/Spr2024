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
        self.nxt = None
class Container():
    def __init__(self):
        self.first = None
        self.size = 0

    def Insert(self,item):
        if self.Exists(item):
            return False
        else:
            x = Node(item)
            x.nxt = self.first
            self.first = x
            self.size +=1
            return True

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
            return True
            
        current = self.first
        while current.nxt.item != item:
            current = current.nxt
        current.nxt = current.nxt.nxt
        return True
    def Retrieve(self, item):
        current = self.first
        while current:
            if item == current.item:
                return current.item
            current = current.nxt
        return None



# class Container:
#     def __init__(self):
#         self.first = None

#     def Insert(self,x):
#         if self.Exists(x):
#             return False
#         else:
#             self.x.next = self.first
#             self.first = self.x
#             return True

#     def Exists(self, x):
#         current = self.first
#         while current:
#             if current == x:
#                 return True
#             current = current.next
#         return False

#     def Retrieve(self, x):
#         for item in self.A:
#             if item ==x:
#                 return item
#         return None

#     def Size(self):
#         return len(self.A)

#     def __iter__(self):
#         for i in self.A:
#             yield i

#     def Delete(self, item):
#         if not self.Exists(item):
#             return False
#         if item == self.start.item:
#             self.start = self.start.next
#             return True
#         # self.first or self.start?
#         current = self.first
#         while not (current.next == item):
#             current = current.next
#         current.next = current.next.next
#         return True




def main():
    # insert
    c = Container()
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
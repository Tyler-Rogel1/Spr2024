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




class Container:
    def __init__(self):
        self.A = []

    def Insert(self,x):
        if self.Exists(x):
            return False
        else:
            self.A.append(x)
            return True

    def Exists(self, x):
        for item in self.A:
            if item==x:
                return True
        return False

    def Retrieve(self, x):
        for item in self.A:
            if item ==x:
                return item
        return None

    def Size(self):
        return len(self.A)

    def __iter__(self):
        for i in self.A:
            yield i

    def Delete(self, dummyStudent):
        if not self.Exists(dummyStudent):
            return False
        for i in self.A:
            if i == dummyStudent:
                self.A.remove(i) 
        return True




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
    print("The average age is: ", totalAge/c.Size())
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
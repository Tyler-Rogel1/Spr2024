import time
class Student:
    def __init__(self):


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
        for i in range(len(self.A)):
            if self.A[i] == dummyStudent:
                # IDK how accurate this next line is
                self.A[i].pop() 




def main():
    c = Container()
    t1 = time.time()
    fin = open("FakeNames.txt", "r")
    for line in fin:
        words = line.split()
        s = Student(words[0], words[1], words[2],words[3], words[4] )
        ok = c.Add(s)
        if not ok:
            print("not ok")
        
    t2 = time.time()
    print("total time is: ", (t2-t1))


    totalAge = 0
    for item in c:
        age = item.age
        totalAge += age
    print("The average age is: ", totalAge/c.size())
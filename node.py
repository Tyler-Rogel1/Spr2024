class Node:
    def __init__(self, item, nxt):
        self.item = item
        self.nxt = nxt
class LinkedList():
    def __init__(self):
        self.first = None
        self.size = 0

    def Insert(self,item):
        n = Node(item,self.first)
        self.first = n
        self.size += 1

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
        for item in self:
            if value == item:
                return True
            return False

    def Delete(self, item):
        if not self.Exists(item):
            return False
        if self.first.item == item:
            self.first = self.first.nxt
            return True
            
        current = self.first
        while current.nxt.iten != item:
            current = current.nxt
        current.nxt=current.nxt.nxt
        return True
    def Retrieve(self, item):
        current = self.mFirst
        while current is not None:
            if item == current.item:
                return current.item
            current = current.nxt
        return None

def main():
    ll = LinkedList()
    ll.Insert("John")
    ll.Insert("Sally")
    ll.Insert("Bob")
    for s in ll:
        print(s)

main()
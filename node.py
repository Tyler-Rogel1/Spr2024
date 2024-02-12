class Node:
    def __init__(self, item, nxt):
        self.item = item
        self.nxt = nxt
class LinkedList():
    def __init__(self):
        self.first = None

    def Insert(self,item):
        n = Node(item,self.first)
        self.first = n

    def __iter__(self):
        current = self.first
        while current is not None:
            yield current.item
            current = current.nxt
        
        
def main():
    ll = LinkedList()
    ll.Insert("John")
    ll.Insert("Sally")
    ll.Insert("Bob")
    for s in ll:
        print(s)

main()
# directed and non weighted graph class
class Graph:
    def __init__(self, vertices):
        self.neighbors = [[]] * vertices

    def addEdge(self, v0, v1):
        self.neighbors[v0].append(v1)

    def isEdge(self, v0, v1):
        return v1 in self.neighbors[v0]

    def findNeighbors(self, v):
        return self.neighbors[v]

# breadth first search
    def findPath(self, v0, v1):

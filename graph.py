# directed and non weighted graph class
class Graph:
    def __init__(self, vertices):
        self.neighbors = []
        for i in range(vertices):
            self.neighbors.append([])

    def addEdge(self, v0, v1):
        self.neighbors[v0].append(v1)

    def isEdge(self, v0, v1):
        return v1 in self.neighbors[v0]

    def findNeighbors(self, v):
        return self.neighbors[v]

# breadth first search
    def findPath(self, v0, v1):
        From = [-1] *len(self.neighbors)
        Q = []
        From[v0] = v0
        Q.append(v0)
        while Q:
            c = Q.pop(0)
            if c == v1:
                # build path and return it
                path = []
                return path.reverse()
            for n in self.neighbors[c]:
                if From[n] == -1:
                    Q.append(n)
                    From[n] = c
        return None
class Graph:
    def __init__(self, v):
        self.adjMatrix = [[0] * v for _ in range(v)]
        self.vertices = v

    def addEdge(self, f, t, w=1):  # f:from, t: to
        self.adjMatrix[f][t] = w

    def removeEdge(self, f, t, w=0):
        self.adjMatrix[f][t] = w

    def getWeight(self, f, t):
        return self.adjMatrix[f][t]

    def getVertices(self):
        return self.vertices

    def getEdges(self):
        count = 0
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.adjMatrix[i][j] != 0:
                    count += 1
        return count

    def inDegree(self, v):
        count = 0
        for i in range(self.vertices):
            if self.adjMatrix[i][v] != 0:
                count += 1
        return count

    def outDegree(self, v):
        count = 0
        for i in range(self.vertices):
            if self.adjMatrix[v][i] != 0:
                count += 1
        return count

    def display(self):
        print(self.adjMatrix)


if __name__ == '__main__':
    G = Graph(7)
    # before adding edge
    print("before adding edge")
    G.display()
    G.addEdge(0, 1)
    G.addEdge(1, 2)
    G.addEdge(2, 1, 2)
    G.addEdge(3, 5)
    G.addEdge(2, 5)
    # after adding edge
    print("after adding edge")
    G.display()
    G.removeEdge(0, 1)
    # after removing edge
    print("after removing edge")
    G.display()
    print(f"The weight of 2,1 vertices: {G.getWeight(2, 1)}")
    print(f"Total Edges: {G.getEdges()}")
    print(f"In degree of vertex 1: {G.inDegree(1)}")
    print(f"Out degree of vertex 1: {G.outDegree(2)}")

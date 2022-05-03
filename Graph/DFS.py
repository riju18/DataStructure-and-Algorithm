class Graph:
    def __init__(self, v):
        self.adjMatrix = [[0] * v for _ in range(v)]
        self.vertices = v
        self.visited = [0] * self.vertices

    def addEdge(self, f, t, w=1):
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

    def dfs(self, source):
        if self.visited[source] == 0:
            print(f"{source}", end='-')
            self.visited[source] = 1
            for i in range(self.vertices):
                if self.adjMatrix[source][i] == 1 and self.visited[i] == 0:
                    self.dfs(i)

    def display(self):
        print(self.adjMatrix)


G = Graph(7)

G.addEdge(0, 1)
G.addEdge(0, 5)
G.addEdge(0, 6)
G.addEdge(1, 0)
G.addEdge(1, 2)
G.addEdge(1, 5)
G.addEdge(1, 6)
G.addEdge(2, 3)
G.addEdge(2, 4)
G.addEdge(2, 6)
G.addEdge(3, 4)
G.addEdge(4, 2)
G.addEdge(4, 5)
G.addEdge(5, 2)
G.addEdge(5, 3)
G.addEdge(6, 3)

G.display()

print('Sequence:')
G.dfs(0)


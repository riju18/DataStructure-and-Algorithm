class Q:
    def __init__(self):
        self.q_list = []
        self.first = 0
        self.last = 0

    def nq(self, vertex):
        if len(self.q_list) == 0:
            self.first += 1
        self.last += 1
        self.q_list.insert(self.last, vertex)

    def dq(self):
        return self.q_list.pop(0)


class Graph:
    def __init__(self, v):
        self.adjMatrix = [[0] * v for _ in range(v)]
        self.vertices = v
        self.q = Q()
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

    def bfs(self, source):
        s = source
        print(f"source: {s} --> ")
        self.visited[s] = 1
        self.q.nq(s)
        while self.q.q_list:
            s = self.q.dq()
            for i in range(self.vertices):
                if self.adjMatrix[s][i] == 1 and self.visited[i] == 0:  # check edge & mpt visited yet
                    print(f"{i}", end=' - ')
                    self.visited[i] = 1
                    self.q.nq(i)

    def display(self):
        print(self.adjMatrix)


if __name__ == '__main__':
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

    print('Sequence:\n==========')
    G.bfs(0)


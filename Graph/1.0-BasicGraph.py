class Vertex:
    def __init__(self, key):  # create vertex/node
        self.node = key
        self.connectedTo = {}  # all neighbours

    def addNeighbour(self, neighbor, weight=0):
        self.connectedTo[neighbor] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getVertex(self):
        return self.node

    def getWeight(self, neighbor):
        return self.connectedTo[neighbor]

    def __str__(self):
        return str(self.node) + ' connected to ' + str([(x, y) for x, y in self.connectedTo.items()])


class Graph:
    def __init__(self):
        self.vertexList = {}
        self.totalVertex = 0

    def addVertex(self, key):
        self.totalVertex += 1
        vertex = Vertex(key)
        self.vertexList[key] = vertex

    def getVertex(self, node):
        return self.vertexList[node] if node in self.vertexList else "vertex not found"

    def addEdge(self, f, t, weight):
        if f not in self.vertexList:
            self.addVertex(f)
        if t not in self.vertexList:
            self.addVertex(t)

        self.vertexList[f].addNeighbour(self.vertexList[t].node, weight)

    def getVertices(self):
        return self.vertexList.keys()

    def __iter__(self):
        return iter(self.vertexList.values())


g = Graph()
for i in 'abcde':   # add some vertices
    g.addVertex(i)
g.addEdge('a', 'b', 2)  # add edge
g.addEdge('a', 'c', 1)
for i in g:
    print(i)

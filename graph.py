class Graph:

    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def printGraph(self):
        for i in self.graph:
            print(i, " -> ", "->".join(map(str, self.graph[i])))


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.printGraph()
class Node(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src: Node, dest: Node):
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        # Your code here
        return self.weight
    def __str__(self):
        # Your code here
        return self.src.getName() + '->' + self.dest.getName() + ' (' + str(self.getWeight()) + ')'

nodeA = Node('A')
nodeB = Node('B')
edge = WeightedEdge(nodeA, nodeB, 10)
print(edge)
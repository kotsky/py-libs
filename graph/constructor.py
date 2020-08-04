class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

	# O(v + e) T / O(v) S
    def depthFirstSearch(self, array):
        array.append(self.name)
        for name in self.children:
        	name.depthFirstSearch(array)
        return array

	# O(v + e) T / O(v) S
    def breadthFirstSearch(self, array):
        i = 0
        array.append(self)
        length = len(array)
        while i < length:
            for child in array[i].children:
                array.append(child)
            array[i] = array[i].name
            i += 1
            length = len(array)
        return array

'''
	Version 2 of BFS. Through queue + pop(0) - no that efficienct for really big N.
'''

# The fubctions/classes below are to
# build graphs from list/array [1, 2, 3, 4].
# each of those numbers (#job) has dependencies
# as [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]] means #1 1 <- 2 etc..

'''
def createGraph(values, deps):
    graph = Graph(values)
    for dep, value in deps:
        graph.addDep(value, dep)
    return graph
'''

class Graph:
    def __init__(self, values):
        self.nodes = []
        self.graph = {}
        for value in values:
            self.addNode(value)
	for dep, value in deps:		# same as createGraph()
            self.addDep(value, dep)

    def addNode(self, value):
        self.graph[value] = GraphNode(value)
        self.nodes.append(self.graph[value])

    def getNode(self, value):
        if value not in self.graph:
            self.addNode(value)
        return self.graph[value]

    def addDep(self, value, dep):
        valueNode = self.getNode(value)
        depNode = self.getNode(dep)
        valueNode.dependencies.append(depNode)


class GraphNode:
    def __init__(self, value):
        self.value = value
        self.dependencies = []
        

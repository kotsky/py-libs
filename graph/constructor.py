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

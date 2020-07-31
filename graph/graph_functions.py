
# To return array of the path from the root node to
# the given node in the tree.
'''
example: _, path1 = findPath(reportOne, topManager, [], False)
class node:
    def __init__(self, name):
        self.name = name
        self.children = []
'''

def findPath(node_to_find, node, path, flag):
    if node == []:
        return flag, path
    if node.name == node_to_find.name:
        flag = True
    for child in node.directReports:
        if flag:
            break
        flag, path = findPath(node_to_find, child, path, flag)
    if flag:
        path.append(node)
    return flag, path
    

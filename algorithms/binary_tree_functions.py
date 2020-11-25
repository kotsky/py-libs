# validateBst returns True if the given tree is a proper BST
def validateBst(tree):
	def validateBstHelper(tree, min_value, max_value):
		if tree is None:
			return True
		if tree.value < min_value or tree.value >= max_value:
			return False
		leftSide = validateBstHelper(tree.left, min_value, tree.value)
		rightSide = validateBstHelper(tree.right, tree.value, max_value)
		return leftSide and rightSide
	return validateBstHelper(tree, float("-inf"), float("inf"))


# BT traversal methods	
# Input "tree", "array" - root of the tree, [] where to store
# Output "array" - contains output numbers 
'''
[1, 2, 5, 5, 10, 15, 22] inOrderTraverse
[10, 5, 2, 1, 5, 15, 22] preOrderTraverse
[1, 2, 5, 5, 22, 15, 10] postOrderTraverse
'''

# Visit left branch, then current node 
# and then right branch

def inOrderTraverse(tree, array):
    if tree.left is not None:
        inOrderTraverse(tree.left, array)
    array.append(tree.value)
    if tree.right is not None:
        inOrderTraverse(tree.right, array)
    return array
	
	
# Visit node before its child nodes

def preOrderTraverse(tree, array):
    array.append(tree.value)
    if tree.left is not None:
        preOrderTraverse(tree.left, array)
    if tree.right is not None:
        preOrderTraverse(tree.right, array)
    return array
	
	
# Visit node after its child nodes

def postOrderTraverse(tree, array):
    if tree.left is not None:
        postOrderTraverse(tree.left, array)
    if tree.right is not None:
        postOrderTraverse(tree.right, array)
    array.append(tree.value)
    return array


# To split elements from array to have a balanced 
# binary tree (to have the minimal depth of the tree)
# Input "array" - sorted array
# Output "root" - root of the tree
''' 
# Version 1. O(Nlog(N)) T / O(N) S
def minHeightBst(array):
    return minHeightBstHelper(None, array)

def minHeightBstHelper(root, array):
    left = 0
    right = len(array)-1
    value = (right + left) // 2
    if root is None:
        root = BST(array[value])
    else:
    	if len(array) == 1:
		root.insert(array[0])
		return
	elif len(array) < 1:
		return
    root.insert(array[value])
    minHeightBstHelper(root, array[left:value])
    minHeightBstHelper(root, array[value + 1:right+1])
    return root
'''

# Version 2. O(N) TS
# The difference with v1 is that here
# we execute function in place (at 
# each next node), where in v1 we 
# insert new nodes with log(N)
# traversing.

def minHeightBst(array):
    return minHeightBstHelper(array)

def minHeightBstHelper(array):
    if len(array) < 1:
        return None
    start = 0
    end = len(array)-1
    value = (end + start) // 2
    root = BST(array[value])
    root.left = minHeightBstHelper(array[start:value])
    root.right = minHeightBstHelper(array[value+1:end+1])
    return root

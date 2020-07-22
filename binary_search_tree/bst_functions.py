# validateBst returns True if the given tree is a proper BST
def validateBst(tree):
	return validateBstHelper(tree, float("-inf"), float("inf"))

def validateBstHelper(tree, min_value, max_value):
	if tree is None:
		return True
	if tree.value < min_value or tree.value >= max_value:
		return False
	leftSide = validateBstHelper(tree.left, min_value, tree.value)
	rightSide = validateBstHelper(tree.right, tree.value, max_value)
	return leftSide and rightSide


# traversal methods	
# Input "tree", "array" - root of the tree, [] where to store
# Output "array" - contains output numbers 
'''
[1, 2, 5, 5, 10, 15, 22] inOrderTraverse
[10, 5, 2, 1, 5, 15, 22] preOrderTraverse
[1, 2, 5, 5, 22, 15, 10] postOrderTraverse
'''
def inOrderTraverse(tree, array):
    if tree.left is not None:
        inOrderTraverse(tree.left, array)
    array.append(tree.value)
    if tree.right is not None:
        inOrderTraverse(tree.right, array)
    return array

def preOrderTraverse(tree, array):
    array.append(tree.value)
    if tree.left is not None:
        preOrderTraverse(tree.left, array)
    if tree.right is not None:
        preOrderTraverse(tree.right, array)
    return array

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
def minHeightBst(array):
    left = 0
    right = len(array)-1
    middle = (right + left)//2
    root = BST(array[middle])
    minHeightBstHelper(root, array[left:middle])
    minHeightBstHelper(root, array[middle + 1:right+1])
    return root

def minHeightBstHelper(root, array):
    if len(array) == 1:
        root.insert(array[0])
        return
    elif len(array) < 1:
        return
    left = 0
    right = len(array)-1
    value = (right + left) // 2
    root.insert(array[value])
    minHeightBstHelper(root, array[left:value])
    minHeightBstHelper(root, array[value + 1:right+1])



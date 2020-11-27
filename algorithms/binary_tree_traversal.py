# BT traversal methods	
# Input "tree", "array" - root of the tree, [] where to store
# Output "array" - contains output numbers 
'''
[1, 2, 5, 5, 10, 15, 22] in_order_traverse
[10, 5, 2, 1, 5, 15, 22] pre_order_traverse
[1, 2, 5, 5, 22, 15, 10] post_order_traverse
'''

# Visit left branch, then current node 
# and then right branch

def in_order_traverse(tree, array):
    if tree.left is not None:
        in_ordery_traverse(tree.left, array)
    array.append(tree.value)
    if tree.right is not None:
        in_ordery_traverse(tree.right, array)
    return array
	
	
# Visit node before its child nodes

def pre_order_traverse(tree, array):
    array.append(tree.value)
    if tree.left is not None:
        pre_order_traverse(tree.left, array)
    if tree.right is not None:
        pre_order_traverse(tree.right, array)
    return array
	
	
# Visit node after its child nodes

def post_order_traverse(tree, array):
    if tree.left is not None:
        post_order_traverse(tree.left, array)
    if tree.right is not None:
        post_order_traverse(tree.right, array)
    array.append(tree.value)
    return array
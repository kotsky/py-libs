# BT traversal methods	
# Input "tree", "array" - root of the tree, [] where to store
# Output "array" - contains output numbers 
'''
[1, 2, 5, 5, 10, 15, 22] in_order_traverse
[10, 5, 2, 1, 5, 15, 22] pre_order_traverse
[1, 2, 5, 5, 22, 15, 10] post_order_traverse


root = TreeNode(10)
root.left = TreeNode(7)
root.right = TreeNode(12)
root.left.left = TreeNode(5)
root.left.right = TreeNode(8)
root.right.right = TreeNode(20)
root.left.left.right = TreeNode(6)
root.left.left.right.left = TreeNode(5.5)
root.right.left = TreeNode(11)

             10
           /    \
          7     12
         / \    / \
        5   8  11  20
         \
          6
         /
        5.5

# in_order_traverse_iterative(root)  # 5 5.5 6 7 8 10 12 20
# dfs_traverse_iterative(root)    # 10 7 5 6 5.5 8 12 11 20 

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


def dfs_traverse_iterative(node):
    stack = [node]
    # node_to_explore = node
    while stack:
        node_to_explore = stack.pop()
        print(node_to_explore.value, end=" ")
        if node_to_explore.right is not None:
            stack.append(node_to_explore.right)
        if node_to_explore.left is not None:
            stack.append(node_to_explore.left)


def in_order_traverse_iterative(node):
    stack = []
    node_to_explore = node
    while True:
        if node_to_explore is not None:
            stack.append(node_to_explore)
            node_to_explore = node_to_explore.left
        else:
            if stack:
                node_to_explore = stack.pop()
                print(node_to_explore.value, end=" ")
                node_to_explore = node_to_explore.right
            else:
                break

""" BT transformation to -> X

	- flatten_binary_tree(root) -> return DLL with its head,
	which is built from left to write of BT.
	- invert_binary_tree(root) -> invert BT (swap left with right)

"""


# class BinaryTree:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right


# input "root" - BT root node
# output "new_head" - DLL head

def flatten_binary_tree(root):

    def flatten_binary_tree_helper(node, head, left_node):
        if node.left is not None:
            head, left_node = flatten_binary_tree_helper(node.left, head, left_node)
        if head is None:
            head = node
        node.left = left_node
        if left_node is not None:
            left_node.right = node
        left_node = node
        if node.right is not None:
            head, left_node = flatten_binary_tree_helper(node.right, head, left_node)
        return head, left_node

    if root is None or (root.left is None and root.right is None):
        return root
    new_head = None
    new_head, _ = flatten_binary_tree_helper(root, new_head, None)
    return new_head


# input "root" - BT root node
# return: nothing

def invert_binary_tree(tree):
    
    def node_invert(node):
        node.left, node.right = node.right, node.left
        
    node_invert(tree)
    if tree.left is not None:
        invert_binary_tree(tree.left)
    if tree.right is not None:
        invert_binary_tree(tree.right)

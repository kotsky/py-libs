"""Binary Search Tree

In this tree each node has max 2 childs and 
following condition is applied 
`node.left.value < node.value <= node.right.value`.

Methods:
	bst = BST(value)
	bst.insert(value)
	bst.contains(value) - check if that value is in bst
	bst.remove(value)
	min_value = bst.getMinValue() - get min value from that bst

Example:
	root = BST(10)
	root.left = BST(5)
	root.left.left = BST(2)
	root.left.left.left = BST(1)
	root.left.right = BST(5)
	root.right = BST(15)
	root.right.left = BST(13)
	root.right.left.right = BST(14)
	root.right.right = BST(22)
	root.insert(12)
	root.remove(10)
"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        root = self
        while True:
            if root.value <= value:
                if root.right is not None:
                    root = root.right
                else:
                    root.right = BST(value)
                    break
            else:
                if root.left is not None:
                    root = root.left
                else:
                    root.left = BST(value)
                    break
        return self

    def contains(self, value):
        root = self
        while root is not None:
            if root.value == value:
                return True
            elif root.value < value:
                root = root.right
            else:
                root = root.left
        return False

    def remove(self, value, parent_node=None):
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            else:
                if current_node.left is not None and current_node.right is not None:
                    current_node.value = current_node.right.get_min_value()
                    current_node.right.remove(current_node.value, current_node)
                elif parent_node is None:
                    if current_node.left is not None:
                        current_node.right = current_node.left.right
                        current_node.value = current_node.left.value
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        current_node.value = current_node.right.value
                        current_node.left = current_node.right.left
                        current_node.right = current_node.right.right
                    else:
                        # current_node.value = None
                        pass
                elif parent_node.left == current_node:
                    parent_node.left = current_node.left if current_node.left is not None else current_node.right
                elif parent_node.right == current_node:
                    parent_node.right = current_node.left if current_node.left is not None else current_node.right
                break
        return self

    def get_min_value(self):
        node = self
        while node is not None:
            if node.left is not None:
                node = node.left
            elif node.right is not None:
                node = node.right
            else:
                return node.value

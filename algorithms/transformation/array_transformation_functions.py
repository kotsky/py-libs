"""Transform array to -> X

- create_balanced_bst_from_sorted_array(sorted_array)

"""

# Input "array" - sorted array
# Output "root" - root of the tree
"""
Create a balanced BST from a sorted array.

Or split elements from array to have a balanced 
binary tree.

Example:
    array = [1, 3, 7, 20, 100, 111, 121]
    bst = create_balanced_bst_from_sorted_array(array)
"""

# Time: O(N) / Space: O(log(N)) + O(N) actual bst space

def create_balanced_bst_from_sorted_array(sorted_array):

    class BSTNode:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def _middle_value_selection(sorted_array, node):
        if not len(sorted_array):
            return None

        middle_point = (len(sorted_array)-1) // 2
        node = BSTNode(sorted_array[middle_point])
        node.left = _middle_value_selection(sorted_array[0:middle_point], node)
        node.right = _middle_value_selection(sorted_array[middle_point+1:len(sorted_array)], node)

        return node

    bst = _middle_value_selection(sorted_array, None)
    return bst

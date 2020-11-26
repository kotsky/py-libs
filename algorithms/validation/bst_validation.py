"""BST validation functions

- validate_bst(tree)


"""


# validate_bst(tree) returns True if the given tree is a proper BST
# Input "tree" - tree node
# Output bool True or False

def validate_bst(tree):
	def validate_bst_helper(tree, min_value, max_value):
		if tree is None:
			return True
		if tree.value < min_value or tree.value >= max_value:
			return False
		leftSide = validate_bst_helper(tree.left, min_value, tree.value)
		rightSide = validate_bst_helper(tree.right, tree.value, max_value)
		return leftSide and rightSide
	return validate_bst_helper(tree, float("-inf"), float("inf"))
